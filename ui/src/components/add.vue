<template>

<div class="container">
    <div v-show="(step==1)" class="ico">
    <el-icon @click="addApp()" class="h" :size="size" :color="color" >
      <Paperclip/>
    </el-icon>
    <h3>add app</h3>
    </div>
    <div v-show="(step==2)" class="ico">
    <el-icon @click="addIcon()" class="h" :size="size" :color="color" >
      <Picture/>
    </el-icon>
    <h3>add icon</h3>
    </div>
    <div v-show="(step==3)" class="ico">
    <el-icon @click="clear()" class="h" :size="size" :color="color" >
      <EditPen/>
    </el-icon>
    <h3>edit properties</h3>
    </div>
    <div v-show="(step==4)" class="ico">
    <el-icon class="h" :size="size" :color="color" >
      <Finished/>
    </el-icon>
    <h3>done</h3>
    </div>
</div>
<!-- ........................................................................ -->
<div class="container">
<div v-show="(step==1)" class="input">
  <el-input
      v-model="filePath"
      placeholder="path to file"
      class="input-with-select"
    >
<!--       <template #prepend>
        <el-select v-model="filePath" placeholder="select" style="width: 115px">
          <el-option @click="addApp()"  label="apps" value="~/apps" />
          <el-option @click="addApp()"  label="scripts" value="~/scripts" />
          <el-option @click="addApp()"  label="python scripts" value="~/python scripts" />
        </el-select>
      </template> -->
      <template #append>
        <el-button @click="addApp()" :icon="Paperclip" />
      </template>
    </el-input>
      <div class="i argv">
    <it-input v-model="argv" label-top="argv" placeholder="argv" mask />
  </div>
</div>
<div v-show="(step==2)" class="input">
  <el-input
      v-model="iconPath"
      placeholder="path to icon"
      class="input-with-select"
    >
<!--       <template #prepend>
        <el-select v-model="iconPath" placeholder="select" style="width: 115px">
          <el-option @click="addIcon()" label="icons" value="~/icons" />
        </el-select>
      </template> -->
      <template #append>
        <el-button @click="addIcon()" :icon="Paperclip" />
      </template>
    </el-input>
</div>
<div v-show="(step==3)" class="input">
  <div class="i">
    <it-input v-model="name" label-top="name" placeholder="name" mask />
  </div>

  <div class="i">
    <div class="selc">
      <div class="sp1">categories</div>
      <n-select v-model:value="categories" multiple :options="allowedCategories" placeholder="choose categories" />
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
  <div v-show="typ=='script'&&runner=='python'&&cmd=='defaults'" class="path">
      <el-input
      
      v-model="interpreterPath"
      placeholder="interpreter path"
      class="input-with-select"> 
<!--       <template #prepend>
        <el-select v-model="interpreterPath" placeholder="select" style="width: 115px">
          <el-option @click="addInterpreterPath()" label=".venvs" value="~/.venvs" />
        </el-select>
      </template> -->
      <template #append>
        <el-button @click="addInterpreterPath()" :icon="Paperclip" />
      </template>
    </el-input>
  </div>

    <div v-show="(cmd == 'custom command')">
      <it-input v-model="ccmd" label-top="command" placeholder="command" mask />
    </div>
  

</div>

<div v-show="step==3" class="input">
  <n-radio-group v-model:value="cmd" name="cmd">
      <n-radio-button value="defaults" label="defaults"></n-radio-button>
      <n-radio-button value="custom command" label="custom command"></n-radio-button>
    </n-radio-group>
</div>

<div v-show="(step==4)" class="input">
  <it-button @click="confirm()" class="btn" type="primary" pulse>confirm</it-button>
  <div>
    <el-checkbox-group v-model="places" size="large">
      <el-checkbox-button v-for="p in allowedPlaces" :key="p" :label="p">
        {{ p }}
      </el-checkbox-button>
    </el-checkbox-group>
  </div>
</div>

</div>
<!-- ........................................................................ -->
<div class="container ac">
    <div class="arrows">
    <el-icon @click="back()" class="h" :size="size" :color="color" >
      <CaretLeft/>
    </el-icon>
    <el-icon @click="next()" class="h" :size="size" :color="color" >
      <CaretRight/>
    </el-icon>
    </div>
</div>
<!-- ........................................................................ -->
    <div class="stp">
        <el-steps :active="step" class="step">
            <el-step title="" :icon="Paperclip" />
            <el-step title="" :icon="Picture" />
            <el-step title="" :icon="EditPen" />
            <el-step title="" :icon="Finished" />
        </el-steps>
    </div>

</template>
<!-- ........................................................................ -->
<style scoped>
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
  margin-bottom: .8rem;
}
.sp1{
  margin-bottom: .5rem;
}
.path{

}
.argv{
  margin-top: 5rem;
}
</style>

<script setup>
    import { computed, ref } from 'vue';
    import { NSelect ,NRadioGroup , NRadioButton} from 'naive-ui'
    import { Edit, Picture, Upload, Paperclip, Checked, Finished, CaretLeft, CaretRight, EditPen } from '@element-plus/icons-vue';
   
    const name=ref('');
    const argv=ref('');
    const filePath=ref('');
    const iconPath=ref('');
    const interpreterPath=ref('');
    const cmd=ref('defaults');
    const ccmd=ref('');
    const places=ref(['menu.....','desktop']);
    const allowedPlaces=['menu.....','desktop'];
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
    const allowedCategories=ref([{
          label: "game",
          value: "Game",
          
        },
        {
          label: "graphics",
          value: "Graphics"
        },
        {
          label: "education",
          value: "Education"
        },
        {
          label: "utility",
          value: "Utility"
        },
        {
          label: "development",
          value: "Development"
        },
        {
          label: "network",
          value: "Network"
        },
        {
          label: "system",
          value: "System"
        },
        {
          label: "audio",
          value: "Audio"
        },
        {
          label: "office",
          value: "Office"
        },
        {
          label: "science",
          value: "Science"
        },
        {
          label: "finance",
          value: "Finance"
        },
        {
          label: "emulator",
          value: "Emulator"
        },
        {
          label: "video",
          value: "Video"
        }]);


    function back(){step.value=Math.max(1,step.value-1);}
    function next(){step.value=Math.min(allowedStep(),step.value+1);}
    
    async function addApp(){
      filePath.value = await eel.getFilePath(filePath.value)();
    }

    async function addIcon(){
      iconPath.value = await eel.getIconPath(iconPath.value)();
    }

    async function addInterpreterPath(){
      interpreterPath.value = await eel.getInterpreterPath(interpreterPath.value)();
    }

    async function confirm(){
      var categs = categories.value.join(';');
      var p = places.value.join(';');
      await eel.make(name.value,filePath.value,iconPath.value,interpreterPath.value,cmd.value,ccmd.value,typ.value,runner.value,is_terminal.value,categs,p,argv.value)();
      name.value='';filePath.value='';iconPath.value='';interpreterPath.value='';cmd.value='defaults';ccmd.value='';typ.value='binary';runner.value='bash';is_terminal.value=false;categories.value=[];places.value=['menu.....','desktop'],argv.value='';
      step.value=1;
      
    }

    function clear(){
    name.value='';interpreterPath.value='';cmd.value='defaults';ccmd.value='';typ.value='binary';runner.value='bash';is_terminal.value=false;categories.value=[];places.value=['menu.....','desktop'];
    }

   


</script>
