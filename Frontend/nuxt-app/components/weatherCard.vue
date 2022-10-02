<template>
  <div>
    <v-card elevation="0" max-height="400" class="overflow-auto">
      <v-card-title>
        {{ $dayjs(weatherData.weather_date).format('dddd, DD.MM.YYYY') }}
      </v-card-title>
      <v-card-text>
        <p><strong>{{ weatherData.description }},</strong> Temperatur: {{ (weatherData.temperature - 273.15).toFixed(1) }}°C,
          Min: {{ (weatherData.temperature_max - 273.15).toFixed(1) }}°C / Max: {{ (weatherData.temperature_min -273.15).toFixed(1) }}°C,
          Bewölkung: {{ weatherData.clouds }}%</p>
      </v-card-text>
    </v-card>
  </div>
</template>
<script setup>
  // const baseUrl = 'https://loggik.pythonanywhere.com/api/'
  const baseUrl = 'https://jft1337.pythonanywhere.com/api/'
  // const baseUrl = "http://127.0.0.1:8000/api/";
  // const weatherData = useState('weatherData', () => {})
  const { data: weatherData, pending, refresh, error } = await useFetch(baseUrl + "wetter/")
  
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