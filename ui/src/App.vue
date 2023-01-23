<script setup>
import { NButton , NIcon } from 'naive-ui'
import { ref } from 'vue'
import add from './components/add.vue'

const value = ref('100')
</script>

<template>
  <!-- <it-tabs class="tabs" style="flex: 1">
    <it-tab title="change"><change/></it-tab>
    <it-tab title="add"><add/></it-tab>
    <it-tab title="settings" :disabled="disabledTab"><settings/></it-tab>
  </it-tabs> -->

  <add/>
</template>

<style scoped>
  .tabs{
    height: 100vh;
    width: 100vw;
  }
</style>
