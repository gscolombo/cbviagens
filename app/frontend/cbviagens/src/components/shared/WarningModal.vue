<script setup lang="ts">
import { ref } from 'vue';

import DefaultButton from '../shared/DefaultButtton.vue';

    const state = ref(0);
    defineProps<{
        message: string
    }>();
    
    const open = () => state.value = 1;
    const close = () => state.value = 0;

    defineExpose({ open });
</script>

<template>
    <div v-show="state" class="modal-container">
        <Transition>
            <div v-if="state" class="modal">
                <span class="material-icons-outlined">report_problem</span>
                {{ message }}
                <DefaultButton text="Fechar" bg-color="darkcyan" :action="close"/>
            </div>
        </Transition>
    </div>
</template>

<style scoped lang="scss">
    .v-enter-active {
        transition: transform 0.125s ease;
    }

    .v-enter-from {
        transform: scale(0);
    }

    .modal-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        .modal {
            transition: transform 0.125s ease;
            width: 460px;
            text-align: center;
            background-color: white;
            border-radius: 10px;
            font-family: var(--font-family);
            font-size: 1.5rem;
            padding: 40px 80px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            span {
                font-size: 3rem;
                color: var(--color-background);
            }
        }
    }
</style>