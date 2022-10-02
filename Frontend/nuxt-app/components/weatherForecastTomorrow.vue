<template>
  <div>
    <div v-if="weatherDataTomorrow.length > 0">
    <v-card elevation="0">
      <v-card-title>
        {{ $dayjs(weatherDataTomorrow[0].weather_date).format('dddd, DD.MM.YYYY') }}
      </v-card-title>
      <v-card-text>
        <v-timeline direction="vertical" side="end">
          <v-timeline-item v-for="weatherData in weatherDataTomorrow.slice(2,7)" size="x-small" dot-color="grey-lighten-2" fill-dot icon="mdi-check">
            <template v-slot:opposite>
              <h3>{{ $dayjs.utc(weatherData.weather_date).format('HH:mm') }}</h3>
            </template>
            <h3>{{ weatherData.description }}</h3>
            <h4> {{ (weatherData.temperature - 273.15).toFixed(1) }}°C</h4>
            <p><strong>{{ (weatherData.temperature_max - 273.15).toFixed(1) }}°C</strong> / {{
            (weatherData.temperature_min - 273.15).toFixed(1)
        }}°C </p>
            <p>Regen {{ (weatherData.probability_of_rain*100).toFixed(0) }}%</p>
          </v-timeline-item>
        </v-timeline>
      </v-card-text>
    </v-card>
    </div>
  </div>
</template>
<script setup>
// const baseUrl = 'https://loggik.pythonanywhere.com/api/'
const baseUrl = 'https://jft1337.pythonanywhere.com/api/'
// const baseUrl = "http://127.0.0.1:8000/api/";
// const weatherData = useState('weatherData', () => {})
const { data: weatherDataTomorrow, pending, refresh, error } = await useFetch(baseUrl + "wetter/wetter_morgen/")

definePageMeta({
  layout: "custom",
});

onMounted(async () => {
  await refreshData()
})

async function refreshData() {
  setInterval(async function () {
    await refresh()
  }, 60000);
}
</script>
<style lang="">
    
</style>