<template>
    <v-app>
    <v-app-bar color="green-lighten-2" elevation="0">
        <v-breadcrumbs :items="items">
        </v-breadcrumbs>
        <v-divider vertical></v-divider>
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
    <v-main class="bg-grey-lighten-3">
        <slot />
    </v-main>
    </v-app>
</template>
<script setup>
const items = [
    {
        title: 'Start',
        disabled: false,
        href: '/',
    },
    {
        title: 'Einkaufsliste',
        disabled: false,
        href: '/einkaufsliste',
    },
    {
        title: 'Rezepte',
        disabled: false,
        href: '/rezepte',
    },
]
// const breadcrumbItems = useState("breadcrumbItems", () => 
//  [
//     {
//         text: 'Start',
//         disabled: false,
//         href: '/',
//     },
//     {
//         text: 'Einkaufsliste',
//         disabled: false,
//         href: '/einkaufsliste',
//     },
//     {
//         text: 'Rezepte',
//         disabled: false,
//         href: '/rezepte',
//     },
// ]
// )
</script>
<style>
</style>