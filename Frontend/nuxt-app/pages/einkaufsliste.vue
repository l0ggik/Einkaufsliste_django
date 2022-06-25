<template>
  <!-- <v-app>
    <v-main> -->
      <v-container>
        <v-row justify="center">
          <v-card min-width="150px" class="cardtest">
            <v-toolbar class="bg-green-lighten-2" max-height="10px" height="10px">
              <v-toolbar-title max-height="10px" height="10px"> </v-toolbar-title>
            </v-toolbar>
            <v-card-title class="bg-green-lighten-3">
              Einkaufsliste
            </v-card-title>
            <v-card-text>
              <div v-if="items && !loading">
                <v-row justify="center" v-for="item in items" :key="item.id">
                  <v-btn class="my-2 bg-green-lighten-4 sbutton" @click="deleteEntry(item.id)">{{ item.name }}
                  </v-btn>
                </v-row>
              </div>
                <v-divider class="my-5"></v-divider>
                <v-row justify="center">
                  <v-text-field label="Einkaufswunsch" class="mb-6" v-model="input" hide-details="auto">
                  </v-text-field>
                </v-row>
                <v-row justify="center">
                  <div>
                    <v-btn :disabled="loading" class="bg-green-lighten-5" @click="createEntry">abschicken</v-btn>
                  </div>
                </v-row>
            </v-card-text>
            <v-card-actions>
              <div>
                <v-divider></v-divider>
                <v-btn :disabled="loading" @click="removeAll" class="bg-green-lighten-5">alles entfernen</v-btn>
                <v-divider></v-divider>
              </div>
            </v-card-actions>
          </v-card>
        </v-row>
      </v-container>
    <!-- </v-main>
  </v-app> -->
</template>
<script setup>

definePageMeta({
  layout: "custom",
});

// const baseUrl = 'https://jft1337.pythonanywhere.com/api/'
const baseUrl = 'https://loggik.pythonanywhere.com/api/'
// const baseUrl = "http://127.0.0.1:8000/api/";
let items = useState("items", () => []);
let input = useState("input", () => "");
let loading = useState("loading", () => true);

onMounted(() => {
  getData();
});

async function getData() {
  loading.value = true
  const response = await $fetch(baseUrl + "einkauf/");
  items.value = response;
  loading.value = false
}
async function deleteEntry(id) {
  await $fetch(baseUrl + "einkauf/", {
    method: "DELETE",
    body: id,
  });
  getData();
}
async function createEntry() {
  await $fetch(baseUrl + "einkauf/", {
    method: "POST",
    body: {
      name: input.value,
    },
  });
  getData();
  input.value = "";
}
async function removeAll() {
  await $fetch(baseUrl + "einkauf/remove_all/", {
    method: "DELETE",
  });
  getData();
}
onUnmounted(() => {
});
</script>
<style lang="scss">

  .sbutton {
    text-transform: none !important;
  }
</style>
