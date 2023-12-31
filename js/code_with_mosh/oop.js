/*https://www.youtube.com/watch?v=PFmuCDHHpwk&list=PLTjRvDozrdlxEIuOBZkMAK5uiqp8rHUax&index=3
https://youtu.be/PFmuCDHHpwk?t=1065*/

/***********Object literal**********/
// const circle = {
//     radius : 1,
//     location : {
//         x:1,
//         y:1
//     },
//     draw:function(){
//         console.log('draw')
//     }
// };

// circle.draw();

/***********Factories **********/
function createCircle(radius) {
    return{
        radius,
        draw : function(){
            console.log('draw')
        }
    };
};

const circle = createCircle(1)
circle.draw();

