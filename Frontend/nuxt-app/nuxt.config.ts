// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  css: ['vuetify/lib/styles/main.sass', 'mdi/css/materialdesignicons.min.css'],
  modules: [
    '@nuxtjs/dayjs'
  ],
  build: {
    transpile: ['vuetify'],
  },
  vite: {
    define: {
      'process.env.DEBUG': true,
    },
  },
  // target: 'static',
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    treeShake: true
  },

  dayjs: {
    locales: ['de', 'en'],
    defaultLocale: 'de',
    defaultTimeZone: 'Europe/Berlin',
    plugins: [
      'utc', // import 'dayjs/plugin/utc'
      'timezone' // import 'dayjs/plugin/timezone'
    ] // Your Day.js plugin
  },
  ssr: false
})
