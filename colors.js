var Links = {
  setColor: function(color){
      var alist= document.querySelectorAll('a');
      var i =0;
      while(i<alist.length){
          alist[i].style.color=color;
          i=i+1;
    }
  }
}

var Body = {
  setColor:function (color){
    document.querySelector('body').style.color = color;
  },//객체는 프로퍼티와 프로퍼티사이에 ,를 찍어야함
  setbackgroundcolor:function(color){
    document.querySelector('body').style.backgroundColor = color;
  }
}
function nightDayHanddler(self){
var target = document.querySelector('body');
if(self.value === 'night'){
Body.setbackgroundcolor('black');
Body.setColor('white');
self.value='day';

Links.setColor('powderblue');

} else {
Body.setbackgroundcolor('white');
Body.setColor('black');
self.value='night';

Links.setColor('blue');
}
}
