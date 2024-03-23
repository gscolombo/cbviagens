<script setup lang="ts">
    defineProps<{
      show: boolean;
      text?: string
    }>();
</script>

<template>
    <div v-if="show" class="spinner-container">
        <img src="../../assets/spinner.svg" alt="Loading icon">
        <p>{{ text || '' }}</p>
    </div>
</template>

<style scoped lang="scss"> 
    p {
        font-family: var(--font-family);
    }
</style>