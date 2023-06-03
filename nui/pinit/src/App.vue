<script setup>
import { provide, ref, watch } from 'vue'
import add from './components/add.vue'
import edit from './components/edit.vue';

var loaded=false

const toggleIconsValue=ref('light')

const menuIcons=ref({})
const desktopIcons=ref({})

provide('menuIcons',menuIcons)
provide('desktopIcons',desktopIcons)

async function init(){
    loaded=false
    await loadMenu()
    await loadDesktop()
    var theme=await eel.getTheme()()
    if (theme) {toggleIconsValue.value=theme} else {toggleIconsValue.value='light'}
    loaded=true

  }

  async function loadMenu(){
    var m=await eel.loadMenu()()
    menuIcons.value=m.split(';;;')
  }

  async function loadDesktop(){
    var d=await eel.loadDesktop()()
    desktopIcons.value=d.split(';;;')
  }

  async function changeTheme(){
    if (loaded) {
      await eel.changeTheme(toggleIconsValue.value)()
      await loadMenu()
      await loadDesktop()
    }
  }

  init()
watch(toggleIconsValue, changeTheme)

</script>

<template @iconChange="init">

  <div id="c" :class="toggleIconsValue">
    <div class="tmc">
      <div class="tm">
      <it-toggle v-model="toggleIconsValue" icons :options="['light', 'dark']">
  <template #light>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="h-full transition-all duration-100 ease-out"
      :class="{
        'fill-yellow-600/40 stroke-yellow-500':
          toggleIconsValue === 'light',
      }"
      stroke="gold"
      fill="gold"
      viewBox="0 0 24 24"
      stroke-width="3"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
      />
    </svg>
  </template>
  <template #dark>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="h-full transition-all duration-500 ease-out"
      :class="{
        'fill-indigo-400/30 stroke-blue-800':
          toggleIconsValue === 'dark',
        'fill-gray-600/40': toggleIconsValue !== 'dark',
      }"
      stroke="indigo"
      fill="indigo"
      viewBox="0 0 24 24"
      stroke-width="2"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
      />
    </svg>
  </template>
</it-toggle>
    </div>
    </div>

    <div class="tabs">
      <it-tabs class="tabs" style="flex: 1">
        <it-tab class="" title="edit"><edit/></it-tab>
        <it-tab class="" title="add"><add/></it-tab>
    </it-tabs>
    </div>


  </div>


</template>

<style scoped>
  *{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  .tabs{

    margin-top: 1.5rem;
  }
  .tm{
    height: 1rem;
    width: 5rem;
    margin-top: 1rem;
    padding-right: 6.2rem;
  }
  .tmc{
    width: 90%;
    margin: auto;
    display: flex;
    justify-content: flex-end;
  }
  #c{
    width: 100vw;
    height: 100vh;
  }
  #c.dark{
    background-color: black;
  }
</style>

