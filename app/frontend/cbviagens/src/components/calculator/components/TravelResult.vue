<script setup lang="ts">
import type { DataModel } from '@/models/data.model';

    defineProps<{
        type: "economic" | "fast"
        bench: "seat" | "bed"
        data: DataModel
    }>();

    const realCurrencyFormat = new Intl.NumberFormat('pt-BR', {style: 'currency', currency: 'BRL'});
</script>

<template>
    <div class="result">
        <div class="travel-info" :style="{backgroundColor: type === 'economic' ? 'var(--color-economy)' : 'var(--color-confort)'}">
            <span class="material-icons-outlined">{{type === 'fast' ? 'speed' : 'savings'}}</span> 
            <div class="info">
                <p>{{ data.name }}</p>
                <p>{{ bench === 'seat' ? `Poltrona: ${data.seat} (convencional)` : `Leito: ${data.bed} (Completo)` }}</p>
                <p>Tempo estimado: {{ data.duration + 'h' }}</p>
                <p>Data de chegada (estimada): {{ data.estimated_arrival_date }}</p>
            </div>
        </div>
        <div class="price" :style="{backgroundColor: type === 'economic' ? 'var(--color-economy)' : 'var(--color-confort)'}">
            <p>Preço</p>
            <p>{{ realCurrencyFormat.format(bench === 'seat' ? data.price_econ : data.price_confort) }}</p>
        </div>
    </div>
</template>

<style scoped lang="scss">
    .result {
        --color-confort: rgb(200,200,200);
        --color-economy: rgb(240,240,240);
        display: flex;
        gap: 10px;
        width: 100%;
        .travel-info {
            display: flex;
            align-items: center;
            border-radius: 5px;
            width: 75%;
            span {
                padding: 36px 20px;
                color: white;
                font-size: 3rem;
                background-color: darkcyan;
                border-radius: 5px 0 0 5px;
            }
            .info {
                margin-left: 20px;
                min-width: max-content;
                p {
                    font-family: var(--font-family);
                    font-size: 1rem;
                    &:first-of-type {
                        text-transform: uppercase;
                        font-weight: bold;
                    }
                }
            }
        }
        .price {
            padding: 20px;
            width: 25%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 5px;
            p {
                font-family: var(--font-family);
                font-size: 1.125rem;
                &:first-of-type {
                    font-weight: bold;
                }
                &:last-of-type {
                    color: var(--font-color-sec);
                }
            }
        }
    }
</style>