<template>
  <div class="mx-5">
    <h1 class="eshopname">
      {{eshop_name}}
    </h1>
    <v-card
      class="mx-auto"
      max-width="500"
    >
    <v-list>
        <v-list-group
          v-for="product in eshop"
          :key="product.id"
          v-model="product.active"
          no-action
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title v-text="product.data.name"></v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="product in eshop"
            :key="product.id"
          >
            <v-list-item-content>
              <v-list-item-title v-text="product.url"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'Products',

  props: ['eshop', "eshop_name"],

  computed()  {
    tempList = null,
  },

  created() {
    console.log(this.eshops)
  },

  data() {
    return {
      something: 0
    }
  },
};
</script>

<style scoped>
.eshopname  {
  text-align: center;
}
</style>
