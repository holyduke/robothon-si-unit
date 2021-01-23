<template>
  <div>
    {{eshopname}}: {{product.name}}
    <price :price="product.price"/>
  </div>
</template>

<script>
import price from './Price'

export default {

  name: 'SimiliarListing',

  props: ['product', 'eshopname'],

  components: {
    price
  }
};
</script>

<style>
</style>
