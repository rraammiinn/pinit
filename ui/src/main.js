import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './style/main.css'

import Equal from 'equal-vue'
import 'equal-vue/dist/style.css'


const app = createApp(App)

app.use(ElementPlus)
app.use(Equal)

app.mount('#app')
