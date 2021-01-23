<template>
  <v-chip
      class="ma-2"
      color="primary"
      outlined
      pill
    >
      <v-icon  left>
        mdi-cash
      </v-icon>
      {{price}} CZK
    </v-chip>
</template>

<script>
export default {
  props:  ['price'],
  name: 'Price',
};
</script>

<style>
</style>
