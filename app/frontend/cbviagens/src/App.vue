<script setup lang="ts">
import LeftPanel from './components/LeftPanel.vue';
import CalculatorContainer from './components/calculator/CalculatorContainer.vue';
</script>

<template>
  <div class="wrapper">
    <LeftPanel />
    <main>
      <CalculatorContainer />
    </main>
  </div>
</template>

<style scoped>
  .wrapper {
    max-width: 100vw;
    max-height: 100vh;
    overflow-x: hidden;
    display: grid;
    grid-template-columns: max(min(25vw, 250px), 200px) 1fr;
  }

  main {
    min-height: 100vh;
    margin-top: 10vh;
    background-color: whitesmoke;
    box-shadow: inset 0px 4px 5px -2px rgba(0,0,0,0.5);
  }
</style>
