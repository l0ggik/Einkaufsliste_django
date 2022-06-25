<template>
    <v-app>
    <v-app-bar color="green-lighten-5" elevation="0">
        <v-breadcrumbs :items="items">
        </v-breadcrumbs>
        <v-divider vertical></v-divider>
        <!-- <NuxtLink to="/">Start</NuxtLink>
        <NuxtLink to="/einkaufsliste">Einkaufsliste</NuxtLink>
        <NuxtLink to="/test">Test</NuxtLink> -->
        <v-breadcrumbs>
            <v-menu>
                <template v-slot:activator="{ props }">
                    <v-btn
                    v-bind="props"
                    >
                    Weitere Listen
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item>
                    <v-list-item-title>Eigene Listen kommen bald</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-breadcrumbs>
    </v-app-bar>
    <v-main>
        <slot />
    </v-main>
    </v-app>
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