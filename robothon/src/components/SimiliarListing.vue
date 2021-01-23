<template>
  <div>
    {{eshopname}}: {{product.name}}
    <br>
    Price: {{product.price}} CZK
  </div>
</template>

<script>
export default {

  name: 'SimiliarListing',

  props: ['product', 'eshopname']
};
</script>

<style>
</style>
