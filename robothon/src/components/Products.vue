<template>
  <div class="mx-5">
    <h1 class="eshopname">
      {{eshopname}}
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
              <v-list-item-title v-text="product.name"></v-list-item-title>
            </v-list-item-content>
          </template>

          <h3 class="ml-2">Same products in {{eshopname}}</h3>
          <v-list-item
            v-for="duplicatID in product.duplicates"
            :key="duplicatID"
          >
            <v-list-item-content >
              <v-list-item-title >
                Price: {{findByIdInEshop(duplicatID, eshops[eshopname]).price}} CZK         
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          
          <h3 class="ml-2" >Same products by competitions</h3>
            <v-list-item v-for="(item, key) in product.similar_listings" :key="key">
              <v-list-item-content>
                <v-list-item-title >
                  <similiar-listing :eshopname="key" :product="findByIdInEshop(product.similar_listings[key], eshops[key])" />                  
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
        </v-list-group>
      </v-list>
    </v-card>
  </div>
</template>

<script>
import SimiliarListing from './SimiliarListing'

export default {
  name: 'Products',

  props: ['eshops','eshop', "eshopname"],

  computed:  {
    tempList: function() {
      return []
    } 
  },

  created() {
    console.log(this.eshops)
  },

  data() {
    return {
    }
  },

  methods: {
    findByIdInEshop(id_tosearch, eshop) {
      console.log("eshop",eshop)
      console.log("looking for id",id_tosearch)
      let foundproduct = eshop.find(product => {
        return product.id == id_tosearch
      })
      return foundproduct;
    }
  },

  components: {
    SimiliarListing
  }
};
</script>

<style scoped>
.eshopname  {
  text-align: center;
}
</style>
