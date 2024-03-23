<template>
    <div class="panel">
        <img class="logo" src="../assets/logo.png" alt="Logo - CB Viagens">
        <ul class="menus">
            <li class="menu">
                <span class="material-icons-outlined">calculate</span>
                Calculadora de Viagem
            </li>
        </ul>
    </div>
</template>

<style scoped>
    .panel {
        width: 100%;
        height: 100%;
        background-color: var(--color-background);
    }

    .panel img.logo {
        width: 100%;
        padding: 20px 30% 20px 20px;
    }

    .panel .menus .menu {
        color: var(--font-color-main);
        font-family: var(--font-family);
        list-style: none;
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 0 5%;
        cursor: pointer;
    }

    .panel .menus .menu span {
        transition: transform 0.15s;
    }

    .panel .menus .menu:hover span {
        transform: scale3d(1.1, 1.1, 1.1);
    }
</style>