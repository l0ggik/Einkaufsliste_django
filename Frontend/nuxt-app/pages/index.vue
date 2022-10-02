<template>
    <!-- <v-app>
        <AppBar/>
        <v-main> -->
            <div>
            <v-card elevation="0">
                <v-card-text>
                    <weatherCard />
                </v-card-text>
            </v-card>
            <v-container background-color="green-lighten-5">
                <v-row>
                    <v-col cols="12" md="3">
                    </v-col>
                    <v-col cols="12" md="3">
                        <weatherForecastCard />
                    </v-col>
                    <v-col cols="12" md="3">
                    </v-col>
                    <v-col cols="12" md="3">
                        <wasteEventsCard />
                    </v-col>
                    <!-- <v-col cols="12" md="4" class="bg-blue">
                        <weatherCard />
                    </v-col>
                    <v-col cols="12" md="4" class="bg-red">
                        <weatherCard />
                    </v-col> -->
                </v-row>
            </v-container>
            </div>
        <!-- </v-main>
    </v-app> -->
</template>
<script setup>
</script>
<style lang="">
    
</style>