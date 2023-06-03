<template>


<div class="container">

</div>
<!-- ........................................................................ -->
<div class="container">
<div v-show="(step==1)" class="input">
  <div class="iii">
    <div class="iiiii">
      <it-input v-model="filePath" mask label-top="file path" placeholder="path to file"><template #suffixIcon><span class="material-symbols-outlined">attachment</span></template></it-input>
    </div>
    <it-button variant="primary" size="small" @click="addApp()"><template #icon><span class="material-symbols-outlined">add</span></template></it-button>
  </div>

  <div class="i argv">
    <it-input v-model="argv" label-top="argv" placeholder="argv" mask><template #suffixIcon><span class="material-symbols-outlined">tune</span></template></it-input>
  </div>
</div>
<div v-show="(step==2)" class="input">
  <div class="iii">
    <div class="iiiii">
    <it-input v-model="iconPath" mask label-top="icon path" placeholder="path to icon"><template #suffixIcon><span class="material-symbols-outlined">image</span></template></it-input>
  </div>
  <it-button variant="primary" size="small" @click="addIcon()" icon="add"><template #icon><span class="material-symbols-outlined">add</span></template></it-button>
  </div>

  <img v-show="imgUrl" id="icon" :src="imgUrl" alt="">
</div>
<div v-show="(step==3)" class="input">
  <div class="i">
    <it-input v-model="name" label-top="name" placeholder="name" mask><template #suffixIcon><span class="material-symbols-outlined">title</span></template></it-input>
  </div>
  <div class="i">
    <div class="selc">
      <it-select multiselect class="select1" label-top="categories" placeholder="categories" v-model="categories" :options="allowedCategories"/>
    </div>
  </div>
  <div class="c i">
    <it-select class="select" label-top="type" v-model="typ" :options="typs"/>
    


    <it-select v-show="typ=='script'&&cmd=='defaults'" class="select" label-top="type" v-model="runner" :options="runners"/>
    
   

 
    <div class="swchc">
      <div class="sp">terminal ?</div>
      <it-switch class="swch" v-model="is_terminal" label=""  />
    </div>
    
  </div >
  <div v-show="typ=='script'&&runner=='python'&&cmd=='defaults'" class="path iii">
    <div class="iiiii">
      <it-input v-model="interpreterPath" mask label-top="interpreter path" placeholder="path to interpreter"><template #suffixIcon><span class="material-symbols-outlined">create_new_folder</span></template></it-input>
    </div>
    <it-button variant="primary" size="small" @click="addInterpreterPath()"><template #icon><span class="material-symbols-outlined">add</span></template></it-button>
  </div>

    <div v-show="(cmd == 'custom command')">
      <it-input v-model="ccmd" label-top="command" placeholder="command" mask><template #suffixIcon><span class="material-symbols-outlined">terminal</span></template></it-input>
    </div>
  

</div>

<div v-show="step==3" class="input">
    <it-toggle v-model="cmd" :options="['defaults', 'custom command']"/>
</div>

<div v-show="(step==4)" class="input">
  <it-button @click="confirm()" class="btn" variant="primary" pulse>confirm<template #icon><span class="material-symbols-outlined">task_alt</span></template></it-button>
  <div class="chk">
    <it-checkbox variant="primary" label="menu" v-model="menu" />
    <it-checkbox variant="primary" label="desktop" v-model="desktop" />


  </div>
</div>

</div>
<!-- ........................................................................ -->
<div class="container ac">
    <div class="arrows">
      <it-button variant="primary-text" @click="back()"><template #icon><span class="material-symbols-outlined">keyboard_double_arrow_left</span></template></it-button>
      <it-button variant="primary-text" @click="next()"><template #icon><span class="material-symbols-outlined">keyboard_double_arrow_right</span></template></it-button>
    </div>
</div>
<!-- ........................................................................ -->

</template>
<!-- ........................................................................ -->
<style scoped>
img{
  border-radius: 1rem;
  margin:auto ;
  margin-top: 5rem;
  width: 50%;
  height: 50%;
}
.stp{
width: 100vw;
display: flex;
justify-content: center;
position: fixed;
bottom: 1rem;
}
.step{
    justify-self: center;
    width: 90vw;
    margin: auto;
}
.container{
    width: 100vw;
    text-align: center;
    padding-top: 1rem;
}
.arrows{
    width: 90%;
    display: flex;
    justify-content: space-between;
    margin: auto;
}
.h:hover{
    color: blue;
    cursor:pointer;
}
.input{
  width: 90vw;
  margin: auto;
  margin-bottom: 1rem;
}
.i{
  margin-bottom: 1rem;
}
.btn{
  margin: auto;
  margin-bottom: 1rem;
}
.ac{
  position: fixed;
  bottom: 3rem;
}
.select{
  z-index: 500;
}
.select1{
  z-index: 1000;
}
.c{
  display:flex;
  justify-content: space-between;
  align-items: flex-end;
}
.swchc{
  display: flex;
  flex-direction: column;
  align-items: flex-end;

}
.selc{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.swch{

}
.sp{
  margin-bottom: 1.2rem;
  font-size: .9rem;
}
#c.dark .sp{
  color: white;
}
.sp1{
  margin-bottom: .5rem;
}
.path{

}
.argv{
  margin-top: 5rem;
}
.chk{
  display: inline-block;
}
.iii{
  display: flex;
  align-items: end;
  justify-content: space-between;
  justify-items: stretch;
  gap: 1rem;
}
.iiiii{
  flex-grow: 1;
}








* ::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 0px rgba(0,0,0,0.3);
	background-color: rgba(0,0,0,0);
  border-radius: .125rem;
  
}

* ::-webkit-scrollbar
{
	width: .25rem;
	background-color: rgba(0,0,0,0);
}

* ::-webkit-scrollbar-thumb
{
	background-color: #F90;	
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


#c.dark * ::-webkit-scrollbar-track
{
	background-color: rgba(0,0,0,0);
}

#c.dark * ::-webkit-scrollbar
{
	background-color: rgba(0,0,0,0);
}
</style>

<script setup>
    import { computed, ref, inject } from 'vue';

    const menuIcons=inject('menuIcons')
    const desktopIcons=inject('desktopIcons')


    const imgUrl=ref('')
    const menu=ref(true)
    const desktop=ref(true)
    const name=ref('');
    const argv=ref('');
    const filePath=ref('');
    const iconPath=ref('');
    const interpreterPath=ref('');
    const cmd=ref('defaults');
    const ccmd=ref('');
    const places=ref('menu;desktop');
    // const allowedPlaces=['menu.....','desktop'];
    const typ=ref('binary');
    const typs=ref(['binary','script']);
    const runner=ref('bash');
    const runners=ref(['bash','sh','zsh','xonsh','enaml','python','fish']);
    const is_terminal=ref(false);
    const step = ref(1);
   
    const allowedStep=()=>{
        if (name.value && (cmd.value=='defaults' || ccmd.value)){return 4}
        else if(iconPath.value){return 3}
        else if(filePath.value){return 2}
        else {return 1}
      };
      

    const size=ref('3rem');
    const color =ref('black');


    const categories=ref([]);
    const allowedCategories=ref(["Game","Graphics","Education","Utility","Development","Network","System","Office","Science","Finance","Emulator","Video"]);



    function back(){step.value=Math.max(1,step.value-1);}
    function next(){step.value=Math.min(allowedStep(),step.value+1);}
    
    async function addApp(){
      filePath.value = await eel.getFilePath(filePath.value)();
    }

    async function addIcon(){
      var icon=await eel.getIconPath(iconPath.value)();
      if (icon){
        iconPath.value = icon
        imgUrl.value = `./icons/${iconPath.value.split('/').slice(-1)}`;
      }
    }

    async function addInterpreterPath(){
      interpreterPath.value = await eel.getInterpreterPath(interpreterPath.value)();
    }

    async function confirm(){
      if (menu.value && desktop.value){places.value='menu;desktop'} else if (menu){places.value='menu'} else if (desktop){places.value='desktop'} else{places.value=''}
      var categs = categories.value.join(';');
      await eel.make(name.value,filePath.value,iconPath.value,interpreterPath.value,cmd.value,ccmd.value,typ.value,runner.value,is_terminal.value,categs,places.value,argv.value)();
      name.value='';filePath.value='';iconPath.value='';interpreterPath.value='';cmd.value='defaults';ccmd.value='';typ.value='binary';runner.value='bash';is_terminal.value=false;categories.value=[];places.value='menu;desktop',argv.value='';
      step.value=1;
      await init()
    }

    function clear(){
    name.value='';interpreterPath.value='';cmd.value='defaults';ccmd.value='';typ.value='binary';runner.value='bash';is_terminal.value=false;categories.value=[];places.value=['menu.....','desktop'];imgUrl.value='icon.svg';
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


</script>
