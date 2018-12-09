import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import colors from 'vuetify/es5/util/colors'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
  iconfont: 'md',
  theme: {
    primary: colors.orange.lighten3, // #FFCC80
    secondary: colors.amber.lighten4, // #FFECB3
    accent: colors.teal.base // #009688
  }
})
