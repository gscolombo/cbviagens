#!/bin/bash

trap stopServers INT

stopServers() {
    printf "\nStopping servers...\n"
    ps -ef | grep -e node -e npm -e python | awk '{print $2}' | xargs kill -9 >/dev/null 2>&1
    echo "Done, bye!"
}

startBackendServer()
{  
    cd backend/cbviagens_api/
    echo "Configuring backend server"
    echo "Installing dependencies..."
    pip install -r requirements.txt &&
    echo "Migrating database..."
    python3 manage.py migrate &
    wait $!
    echo "Starting server..."
    python3 manage.py runserver localhost:3000 >/dev/null 2>&1 &
    if (ps -ef | grep python >/dev/null 2>&1);
    then printf "Backend online! Test the API visiting http://localhost:3000/travels/test.\n\n"
         cd ../../
         return 0
    else return 1
    fi
}

startFrontEndServer()
{
    cd frontend/cbviagens/
    echo "Configuring frontend server"
    echo "Updating Node.JS"
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash >/dev/null &&
    export NVM_DIR="$HOME/.nvm" >/dev/null
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" >/dev/null
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" >/dev/null
    nvm install 20 --latest-npm &&
    echo "Installing dependencies..."
    npm install &&
    chmod u+x node_modules/.bin/vite
    echo "Starting server..."
    if (npm run dev >/dev/null & node=$!)
    then printf "Good to go! Visit http://localhost:8080 to see the frontend.\nPress CTRL+C to exit.\n\n"
         wait $node
    else stopServers
    fi
}

printf "Starting servers...\n\n"
startBackendServer && startFrontEndServer

