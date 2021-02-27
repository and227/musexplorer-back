<template>
  <ul>
    <li>Albums:</li>
    <hr />
    <li v-for="(name, index) in groupsAndAlbums" v-bind:key="index">
      {{ name.name }}
    </li>
  </ul>
</template>

<script>
export default {
  props: ['groupsAndAlbums'],
}
</script>

<style scoped>
ul {
  border: 2px solid black;
  width: 300px;
  padding-left: 0;
}
</style>
