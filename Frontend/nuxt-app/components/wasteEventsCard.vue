<template>
    <div>
        <v-card max-width="300px" elevation="0" height="450" class="overflow-auto">
            <v-card-title>
                Nächste Mülltermine
            </v-card-title>
            <v-card-text v-for="wasteEvent in wasteData">
                <p :class='checkForNextDay($dayjs(wasteEvent.event_date), $dayjs()) ? "bg-green-lighten-3" : ""'>
                    <v-icon  
                        icon="mdi-delete"
                        :color='getTrashcanColor(wasteEvent.name)'
                        large
                    >
                    </v-icon>
                    {{ $dayjs(wasteEvent.event_date).format('dddd, DD.MM.YYYY') }}<br> {{ wasteEvent.name }}
                </p>
            </v-card-text>
        </v-card>
    </div>
</template>
<script setup>
// const baseUrl = 'https://loggik.pythonanywhere.com/api/'
const baseUrl = 'https://jft1337.pythonanywhere.com/api/'
// const baseUrl = "http://127.0.0.1:8000/api/";
// const weatherData = useState('weatherData', () => {})
const { data: wasteData, pending, refresh, error } = await useFetch(baseUrl + "muell/")

onMounted(async () => {
    await refreshData()
})

async function refreshData() {
    setInterval(async function () {
        await refresh()
    }, 60000);
}
function checkForNextDay(date, now) {
    // console.log("Difference", date.diff(now, 'day'))
    if (date.diff(now, 'day') < 1) {
        return true
    }
    else {
        return false
    }
}
function getTrashcanColor(trashcanType) {
    switch (trashcanType) {
        case 'Restabfall 40L-240L(2-wöchentlich)':
            return "grey-darken-1"
        case 'Wertstoff/LVP(2-wöchentlich)':
            return "yellow-darken-2"
        case 'Bioabfall(2-wöchentlich)':
            return "brown-darken-1"
        default:
            return "light-blue-darken-2"
    }
    return "red darken-3"
}
</script>
<style lang="">

    
</style>