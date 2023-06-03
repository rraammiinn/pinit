import { createApp } from 'vue'
import App from './App.vue'
//import ElementPlus from 'element-plus'
//import 'element-plus/dist/index.css'
import './style/main.css'

import Equal from 'equal-vue'
import Config from 'equal-vue/dist/theme/full'

//import 'equal-vue/dist/style.css'



const app = createApp(App)

//app.use(ElementPlus)
app.use(Equal,Config)

app.mount('#app')
