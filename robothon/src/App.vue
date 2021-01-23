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
      <v-text-field
      class="my-5 mx-10"
        label="Search product"
        v-model="search_product"
      ></v-text-field>
      <v-container grid-list-xs class="eshops">
        <Products :eshop="data.alza" eshop_name="Alza"/>
        <Products :eshop="data.czc" eshop_name="CZC"/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import data from "@/dataLoader";
import Products from '@/components/Products.vue';

export default {
  name: 'App',

  created() {
    this.data = data;
    console.log("data",data);
  },

  components: {
    Products,
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped>
  .eshops {
    display: flex;
  }
</style>




