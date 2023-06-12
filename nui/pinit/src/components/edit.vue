<template>
  <div v-show="Object.entries(menuIcons).length" class="c"><p>menu icons :</p></div>
  <div class="scrollmenu">
    <div v-for="menuIcon in menuIcons" @click="getMenuIconDetails(menuIcon.split(',,,')[0])" class="iii">
      <img v-if="menuIcon.split(',,,')[2]" :src="`./menu/${menuIcon.split(',,,')[2]}`" style="width: 100%;height: 100%;" :alt="menuIcon.split(',,,')[1]">
    </div>

</div>


<div v-show="(Object.entries(desktopIcons).length)" class="c"><p>desktop icons :</p></div>
<div class="scrollmenu">
  <div v-for="desktopIcon in desktopIcons" @click="getMenuIconDetails(desktopIcon.split(',,,')[0])" class="iii">
      <img v-if="desktopIcon.split(',,,')[2]" :src="`./desktop/${desktopIcon.split(',,,')[2]}`" style="width: 100%;height: 100%;" :alt="desktopIcon.split(',,,')[1]">
    </div>

</div>

<it-divider style="width: 90%;margin: auto;margin-top: .5rem;" />

<div class="d">
  <div class="detail" v-for="(value,name,index) in details">  <it-input @click="(varient='warning')" v-model="details[name]" :message="name" :key="name" :variant="(index%2 ? 'warning':'success')" class="ixi" ></it-input></div>


</div>
<div class="ddd">
  <div class="ddddd"><p class="p">icon :</p><it-button  @click="selectIcon()" variant="primary" size="small"><template #icon><span class="material-symbols-outlined">image</span></template></it-button></div>
  <div class="ddddd"><p class="p">terminal ?</p><it-switch v-model="Terminal"></it-switch></div>
  <div class="dcc">
    <div class="dc">



      <it-popover id="del" v-show="(path)" >
      <div @click="(removed=false)" class="dc"><span class="material-symbols-outlined spn">delete</span></div>

  <template #content>
    <div v-show="(!removed)" class="p-1">
      <p class="mb-2 ppp">delete icon ?</p>
      <div class="flex justify-end gap-2">
        <it-button outlined variant="danger" size="small" @click="delNo()">no</it-button>
        <it-button size="small" variant="danger" @click="delYes()">yes</it-button>
      </div>
    </div>
  </template>
</it-popover>

    </div>
    <div class="dc"><it-button  outlined @click="clean()" variant="primary" ><template #icon><span class="material-symbols-outlined">cancel</span></template></it-button></div>
    <div class="dc"><it-button  @click="change()" :variant="varient" pulse><template #icon><span class="material-symbols-outlined">task_alt</span></template></it-button></div>
</div>
</div>
</template>

<style scoped>


div.scrollmenu {
  overflow: auto;
  white-space: nowrap;
  width: 90%;
  margin: auto;

}




.iii{
  width: 3.5rem;
  height: 3.5rem;
  display: inline-flex;
  background-repeat: no-repeat;
  background-size:cover;
  border: solid rgb(37, 99, 235) .25rem;
  border-radius: 1rem;
  margin: .5rem;
  margin-top: 1rem;
  padding: .25rem;
}

.iii:hover{
  border-color: gold;
}

.iii:hover{
  width: 4.5rem;
  height: 4.5rem;
  margin-top: 0;
}

.i{

  display: inline;
}





.scrollmenu::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 0px rgba(0,0,0,0.3);
	background-color: #F5F5F5;
  border-radius: .125rem;
  
}

.scrollmenu::-webkit-scrollbar
{
	height: .25rem;
	background-color: #F5F5F5;
}

.scrollmenu::-webkit-scrollbar-thumb
{
	background-color: #ffe767;	
	background-image: -webkit-linear-gradient(45deg,
	                                          rgba(255, 255, 255, .2) 25%,
											  transparent 25%,
											  transparent 50%,
											  rgba(255, 255, 255, .2) 50%,
											  rgba(255, 255, 255, .2) 75%,
											  transparent 75%,
											  transparent);
  border-radius: .125rem;
  height: .25rem;
}


#c.dark .scrollmenu::-webkit-scrollbar-track
{
	background-color: #3F3F46;
}

#c.dark .scrollmenu::-webkit-scrollbar
{
	background-color: #3F3F46;
}




.c{
  width: 90%;
  margin: auto;
  margin-top: 1rem;
}
p{
  font-weight: bold;
}
.d{
  width: 90%;
  border: solid rgb(37, 99, 235) .25rem;
  border-left: none;
  border-right: none;
  border-radius: 0rem;
  margin: auto;
  margin-top: 2rem;
  height: calc(100vh - 31.5rem);
  overflow-y: auto;
  padding: .5rem;
  padding-left: 0;
  text-align: justify;
}




.d::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 0px rgba(0,0,0,0.3);
	background-color: rgba(0,0,0,0);
  border-radius: .125rem;
  
}

.d::-webkit-scrollbar
{
	width: .25rem;
	background-color: rgba(0,0,0,0);
}

.d::-webkit-scrollbar-thumb
{
	background-color: #ffe767;	
	background-image: -webkit-linear-gradient(45deg,
	                                          rgba(255, 255, 255, .2) 25%,
											  transparent 25%,
											  transparent 50%,
											  rgba(255, 255, 255, .2) 50%,
											  rgba(255, 255, 255, .2) 75%,
											  transparent 75%,
											  transparent);
  border-radius: .125rem;
  width: .25rem;
}


#c.dark .d::-webkit-scrollbar-track
{
	background-color: rgba(0,0,0,0);
}

#c.dark .d::-webkit-scrollbar
{
	background-color: rgba(0,0,0,0);
}




.ddd{
  display:flex;
  gap: .5rem;
  justify-content: space-between;
  align-items: flex-end;
  width: 90%;
  margin: auto;
  height: 4rem;
  margin-top: 1rem;
}
.ddddd{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 4rem;
  margin-right: .5rem;
}
.dc{
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
.dcc{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  height: 4rem;
  margin-left: auto;
  gap: .5rem;
}


.ixi{
  padding-bottom: 3rem;
}

.p{
  font-size: .8rem;
}

.ppp{
  padding-bottom: 1rem;
}

.spn{
  color: crimson !important;
}

.spn:hover{
  color: gold !important;
  padding-bottom: .1rem ;

}



.detail{
  padding-bottom: 1rem;
}
</style>


<script setup>
import { computed, inject, ref } from 'vue';

var path=''
var details=ref()
var otherDetails=[]
var varient=ref('primary')
const removed=ref(false)

const menuIcons=inject('menuIcons')
const desktopIcons=inject('desktopIcons')

const Terminal = computed({
  get() {
    return details.value['Terminal']==true || details.value['Terminal']=='true'
  },
  set(val) {
    details.value['Terminal'] = val.toString()
  }})



  //------------------------------------------------------------------------------
  async function getMenuIconDetails (p) {
    varient.value='warning'
    otherDetails=[]
    var m = await eel.getMenuIconDetails(p)()
    m=m.split('\n')
    details.value={}
    for (var i of m){
      if (i.includes('=')){
        i=i.replace('=', ',,,')
        i=i.split(',,,')
        details.value[i[0]]=i[1]
        otherDetails.push([true, i[0]])
      }
      else{
        otherDetails.push([false, i])
      }
    }
    path=p
  }

  async function getDesktopIconDetails (p) {
    varient.value='warning'
    otherDetails=[]
    var d = await eel.getDesktopIconDetail(p)()
    d=d.split('\n')
    details.value={}
    for (var i of d){
      if (i.includes('=')){
        i=i.replace('=', ',,,')
        i=i.split(',,,')
        details.value[i[0]]=i[1]
        otherDetails.push([true, i[0]])
      }
      else{
        otherDetails.push([false, i])
      }
    }
    path=p
  }

  async function selectIcon () {
    var iconPath = await eel.getIconPath()()
    if (iconPath) {
      details.value['Icon']=iconPath
    }
  }

  async function change() {
    if (!path) return;
    var d='';
    for ( const[c,v] of otherDetails){
      if (c){
      d=d+v+'='+details.value[v]+'\n'
    }
    else{
      d=d+v+'\n'
    }
  }
    await eel.change(path,d)()
    await init()
    varient.value='success'
    path=''
    details.value={}
  }


  async function init(){
    await loadMenu()
    await loadDesktop()
  }

  async function loadMenu(){
    var m=await eel.loadMenu()()
    menuIcons.value=m.split(';;;')
  }

  async function loadDesktop(){
    var d=await eel.loadDesktop()()
    desktopIcons.value=d.split(';;;')
  }
 
  function clean(){
    path=''
    details.value={}
    varient.value='primary'
  }
  
  async function delYes(){
    await eel.delete(path)()
    path=''
    details.value={}
    await init()
    removed.value=true
  }

  function delNo(){
    removed.value=true
  }

</script>