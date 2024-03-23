<script setup lang="ts">
    defineProps<{
        text: string
        bgColor: string
        action: ((payload: MouseEvent) => void) | undefined
    }>();
</script>

<template>
    <button type="button" :style="{backgroundColor: bgColor}" @click="action">
        {{ text }}
    </button>
</template>

<style scoped lang="scss">
    button {
        width: 60%;
        margin: 10px auto 0 auto;
        border: none;
        border-radius: 4px;
        padding: 4px 0;
        font-family: var(--font-family);
        font-size: 1rem;
        font-weight: 700;
        cursor: pointer;
        transition: transform 0.125s ease;
        &:hover {
            transform: scale(1.075);
        }
    }
</style>