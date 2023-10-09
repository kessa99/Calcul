/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily:{
        'popins': ['Poppins', 'sans']
      },
      margin: {
        'mept': '80px',
        'mepb': '70px',
        'mepg': '30px',
        'mepd': '30px',
      },
      colors: {
        'footer1': '#111',
        'footer2': '#000',
      },
      maxWidth:{
        'taxmw': '1600px',
        '600px': '600px',
        '430px': '430px'
      },
      gridColumn: {
        '300': '300px',
      },
      topLeftCenter: {
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        position: 'absolute',
      },
      padding:{
        'pt100': '100px 0 0 0',
        'pr20': '0 20px 0 0',
        'pb0': '0 0 0 0',
      },
      fontweight:{
        'fw900':'',
      },
      color:{
        'red':'#dc2626',
      },
      backgroundImage: {
        'back': "url('/src/static/img/back.png')!important",
      },
      width:{
        '640px': '640px',
        '100px': '100px',
        '500px': '500px',
        '400px': '400px',
      },
      height:{
        '400px': '400px'
      },
      keyframes: {
        wiggle: {
          '0%,20%': {  transform: 'translateX(0)' },
          '25%,45%': { transform: 'translateX(-100%)' },
          '50%,70%': { transform: 'translateX(-200%)' },
          '75%,95%': { transform: 'translateX(-300%)' },
          '100%': { transform: 'translateX(-400%)' },
        },
        typing: {
          to: {
            'width': 'width: 0%',
          }
        },
        move: {
          '0%': {transform: 'translate(-15px, 0px)'},
          '50%': {transform: 'translate(0px, -15px)'},
          '100%': {transform: 'translate(-15px, 0px)'},
        }
      },
      animation: {
        'wiggle': 'wiggle 12s infinite ease-in-out',
        'typing': 'typing 3s steps(14) infinite',
        'move': 'move 2.5s linear infinite',
      },
    },
  },
  plugins: [],
};

