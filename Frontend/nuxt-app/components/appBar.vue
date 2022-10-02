<template>
    <div>
        <v-app-bar color="green-lighten-5" elevation="0">
            <v-breadcrumbs :items="items"></v-breadcrumbs>
            <!-- <NuxtLink to="/">Start</NuxtLink>
            <NuxtLink to="/einkaufsliste">Einkaufsliste</NuxtLink>
            <NuxtLink to="/test">Test</NuxtLink> -->
        </v-app-bar>
    </div>
</template>
<script setup>
const items = [
    {
        text: 'Start',
        disabled: false,
        href: '/',
    },
    {
        text: 'Einkaufsliste',
        disabled: false,
        href: '/einkaufsliste',
    },
    {
        text: 'Rezepte',
        disabled: false,
        href: '/rezepte',
    },
]
</script>
<style>
</style>