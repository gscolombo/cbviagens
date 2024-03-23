<script setup lang="ts">
import { shallowRef, ref } from 'vue';

import TravelForm from './components/TravelForm.vue';
import TravelResults from './components/TravelResults.vue';
import WarningModal from '../shared/WarningModal.vue';

import type { DataModel } from '@/models/data.model';
import type { FormDataModel } from '@/models/form-data.model';
import type { ResponseModel } from '@/models/response.model';
    
    let data = shallowRef<DataModel[]>([]);
    let modal = ref<typeof WarningModal | null>(null);
    let resultsPanel = ref<typeof TravelResults | null>(null);

    /**
     * Finds travels based on the provided form data.
     *
     * @param {FormDataModel} data - The form data containing the destination and period.
     * @return {Promise<ResponseModel<{travels: DataModel[]}> | void>} - A promise that resolves to the response model containing the travels data, or void if the data is invalid.
     */
    async function findTravels(data: FormDataModel): Promise<ResponseModel<{travels: DataModel[]}> | void> {
        if (!data || !data.destination || !data.period) {
            modal.value!.open();
            return;
        }

        resultsPanel.value!.loading = true;
        const q = `?city=${data.destination}&departureDate=${data.period}`;
        const response = await fetch(`http://localhost:3000/travels${q}`);
        const json = await response.json() as ResponseModel<{travels: DataModel[]}>;
        return json;
    }
</script>

<template>
    <div class="calculator-container">
        <header>
            <span class="material-icons-outlined truck">
                local_shipping
                <span class="material-icons-outlined arrow">arrow_right_alt</span>
            </span>
            <h1>
                Calculadora de Viagem
            </h1>
        </header>
        <div class="content">
            <TravelForm 
            @search="findTravels($event as FormDataModel)
                     .then(json => data = json?.data.travels ?? []).finally(() => resultsPanel!.loading = false)
            "/>
            <TravelResults ref="resultsPanel" :results="data" @clear="data = []" />
            <WarningModal ref="modal" message="Insira os valores para realizar a cotação."/>
        </div>  
    </div>
</template>

<style scoped lang="scss">
    .calculator-container {
        width: 92.5%;
        height: fit-content;
        margin: 5% auto 0 auto;
        background-color: white;
        border-radius: 0 0 4px 4px;
        display: flex;
        flex-direction: column;
        header {
            background-color: var(--color-background);
            padding: 15px;
            color: var(--font-color-main);
            display: flex;
            align-items: center;
            gap: 10px;
            border-radius: 4px 4px 0 0;
        }
        .content {
            padding: 30px 20px 20px 20px;
            display: grid;
            grid-template-columns: 30% 1fr;
            gap: 20px;
        }
    }

    span.truck {
        position: relative;
    }

    span.arrow {
        position: absolute;
        left: -2.5px;
        top: -2.5px;
        transform: scale(0.5);
    }
</style>
