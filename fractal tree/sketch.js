var slider, angle = radians(20);

function setup(){
	createCanvas(800,400)
	slider = createSlider(0,radians(360),radians(20),0.01);
}

function draw(){
	background(51)
	angle = slider.value();
	stroke(255)
	translate(width/2, height);
	var len = floor(height/4);
	branch(len)
}

function branch(len){
	line(0,0,0,-len);
	translate(0,-len);
	if (len > 3){
		push();
		rotate(angle);
		branch(len*0.67)
		pop();
		push();
		rotate(-angle);
		branch(len*0.67)
		pop();
  }
}
