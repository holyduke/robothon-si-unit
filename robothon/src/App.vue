<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-toolbar-title class="heading">Apify Eshop Matcher</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-select
        class="ma-10"
        :items="items"
        v-model="selected"
        label="Choose eshop view"
      ></v-select>
      <v-container grid-list-xs class="eshops">
        <Products :eshops="data" :eshop="data[selected]" :eshopname="selected"/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import data from "@/dataLoader";
import Products from '@/components/Products.vue';

export default {
  name: 'App',

  data() {
    return {
      items: ['alza', 'czc', 'mironet', 'mall'],
      selected: 'alza'
    }
  },

  created() {
    this.data = data;
    console.log("data",data);
  },

  components: {
    Products,
  },
};
</script>

<style scoped>
  .eshops {
    display: flex;
  }
</style>




