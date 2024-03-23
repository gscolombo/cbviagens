<script setup lang="ts">
import { ref } from 'vue';

import TravelResult from './TravelResult.vue';
import DefaultButtton from '@/components/shared/DefaultButtton.vue';
import LoadingSpinner from '@/components/shared/LoadingSpinner.vue';

import type { DataModel } from '@/models/data.model';

    const loading = ref<boolean>(false);
    type bench = 'seat' | 'bed';
    type result = [DataModel, bench];

    function getResults(data: DataModel[]): [result, result] {
        const type = (economic: number, confort: number) => (economic < confort ? 'seat' : 'bed') as bench;

        // Sorts by duration
        const faster = [data.sort((a, b) => a.duration - b.duration)[0], 'bed'] as result;
        
        // Sorts by price, considering the lower between the confort and economic prices
        // (some ecomonomic prices are lower than confort prices in the dataset)
        const cheaper = [data.sort((a, b) => [a.price_econ, a.price_confort].sort()[0] - [b.price_econ, b.price_confort].sort()[0])[0],
                         type(data[0].price_econ, data[0].price_confort)] as result;
        return [faster, cheaper];
    };

    defineProps<{
        results: DataModel[]
    }>();

    defineExpose({ loading });
</script>

<template>
    <div class="results-panel">
        <LoadingSpinner :show="loading" text="Procurando as melhores opções..."/>
        <p v-if="!results.length && !loading" style="text-align: center;">Nenhum dado selecionado.</p>
        <div v-if="results.length && !loading" class="results">
            <p style="text-align: left; color: var(--font-color-sec);">
                Estas são as melhores alternativas de<br> viagem para a data selecionada
            </p>
            <TravelResult 
                :key="result[0].id" 
                v-for="(result, i) in getResults(results)" 
                :type="!i ? 'fast' : 'economic'"
                :bench="result[1]" 
                :data="result[0]"
                />
        </div>
        <DefaultButtton class="clear-button" text="Limpar" bgColor="orange" :action="() => $emit('clear')" />
    </div>
</template>

<style scoped lang="scss">
    .results-panel {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        p {
            font-size: 1.25rem;
            font-family: var(--font-family);
        }
        .results {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .clear-button {
            position: absolute;
            right: 0;
            bottom: 10px;
            width: 20%;
        }
    }
</style>