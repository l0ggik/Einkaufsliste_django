<template>
    <div>
        <v-card height="450" class="overflow-auto" elevation="0">
            <v-tabs v-model="tab">
                <v-tab value="tomorrow">Morgen</v-tab>
                <v-tab value="dayAfterTomorrow">Übermorgen</v-tab>
            </v-tabs>

            <v-card-text>
                <v-window v-model="tab">
                    <v-window-item value="tomorrow">
                        <WeatherForecastTomorrow />
                    </v-window-item>

                    <v-window-item value="dayAfterTomorrow">
                        <WeatherForecastDayAfterTomorrow/>
                    </v-window-item>
                </v-window>
            </v-card-text>
        </v-card>
    </div>
</template>
<script setup>
    const tab = useState('tab', () => 'tomorrow')
</script>
<style>
    
</style>