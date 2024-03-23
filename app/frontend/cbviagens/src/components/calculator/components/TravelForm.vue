<script setup lang="ts">
import { onMounted, ref, shallowRef } from 'vue';

import DefaultButton from '../../shared/DefaultButtton.vue';

import type { ResponseModel } from '@/models/response.model';
import type { DestinationsModel } from '@/models/destinations.model';

    const today = () => { 
        let date = new Date(), offset = date.getTimezoneOffset();
        date = new Date(date.getTime() - (offset*60*1000))
        return date.toISOString().split('T')[0];
    }
    const getDestinations = async () => (await fetch('http://localhost:3000/travels/destinations/')).json();
    
    let destinations = shallowRef<string[]>([]);
    let select = ref<HTMLSelectElement | null>(null);
    let period = ref<HTMLInputElement | null>(null);

    onMounted(() => {
        getDestinations()
        .then((res: ResponseModel<DestinationsModel>) => destinations.value = res.data.destinations );
    })
</script>

<template>
    <form>
        <h1>
            <span class="material-icons-outlined">savings</span> 
            Calcule o valor da viagem
        </h1>
        <div class="field">
            <label for="destination">Destino</label>
            <select ref="select" name="destination" id="destination" :disabled="destinations.length == 0">
                <option value="" disabled selected>Selecione o destino</option>
                <option :key="index" v-for="(destiny, index) in destinations">
                    {{ destiny }}
                </option>
            </select>
        </div>
        <div class="field">
            <label for="period">Data</label>
            <input ref="period" type="date" name="period" id="period" :min="today()">
        </div>
        <DefaultButton text="Buscar" bg-color="darkcyan" 
        :action="() => $emit('search', {destination: select?.value, period: period?.value})"/>
    </form>
</template>

<style scoped lang="scss">
    form {
        padding: 70px 30px 120px 35px;
        width: 100%;
        background-color: rgba(192,192,192, 0.25);
        display: flex;
        flex-direction: column;
        border-radius: 5px;
        gap: 30px;
    }

    h1 {
        font-family: var(--font-family);
        font-weight: 700;
        font-size: 1.125rem;
        margin-top: 2px;
        color: var(--font-color-text);
        display: flex;
        gap: 5px;
    }

    .field {
        display: flex;
        flex-direction: column;
        label {
            font-family: var(--font-family);
            color: var(--font-color-sec);   
            font-weight: bold;
            font-size: 0.75rem;
        }
        input, select {
            padding: 10px;
            border-radius: 5px;
            outline: none;
            border: none;
            box-shadow: -0.5px -1px 2px 0 rgba(0,0,0,0.25);
            margin-top: 5px;
            margin-left: 2px;
            font-family: var(--font-family);
            color: var(--font-color-sec);
            cursor: pointer;
        }
    }
</style>