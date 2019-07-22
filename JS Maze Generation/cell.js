function index(i,j){
  if (i<0 || j<0 || i > cols-1 || j > rows - 1){
    return undefined;
  }
  return i + (j * cols);
}
function Cell(i, j) {//i is column(x) j is row(y)
	this.i = i;
	this.j = j;
	this.sides = [true,true,true,true];//t,r,b,l
  this.visited = false;
	this.current = false
  this.blocked = false
  this.path = false;
	this.show = function() {//draws the walls of the cell
		var x = this.i*w;
		var y = this.j*w;
		stroke(255)
		if (this.sides[0]){//if t
			line(x,y,x+w,y);
		}
		if (this.sides[1]){//if r
			line(x+w,y,x+w,y+w);
		}
		if (this.sides[2]){//if b
			line(x+w,y+w,x,y+w);
	  }
		if (this.sides[4]){//if l
			line(x,y+w,x,y);
		}
    if(this == grid[0]){//start block green
      noStroke();
      fill(0,255,0,50)
      rect(x,y,w,w);
    }else if(this == grid[grid.length-1]){
      noStroke();
      fill(0,0,255,50)
      rect(x,y,w,w);
    }else if (this.path){
      noStroke();
      fill(160, 140, 255,20);
      //fill(0,255,0,50)
      rect(x,y,w,w);
      // lines
      stroke(255,0,0,200);
      //left = x+w,y+(w/2)+w
      //centre = centreX+w,centreY+w
      //top = x+(w/2)+w,y+w
      //bottom = x+(w/2)+w,y+(w*2)
      //right = x+(w*2),y+(w/2)+w
      var x = (this.i-1)*w;
      var y = (this.j-1)*w;
      x = (this.i-1)*w;
      y = (this.j-1)*w;
      centreX = x+(w/2)
      centreY = y+(w/2)
      var top    = grid[index(i,j-1)];
      var right  = grid[index(i+1,j)];
      var bottom = grid[index(i,j+1)];
      var left   = grid[index(i-1,j)];
      if (top){
        if ((top.path && !top.sides[2]) || ((top == grid[0]) && (!this.sides[0]))) {
          line(centreX+w,centreY+w,x+(w/2)+w,y+w)
        }
      }
      if (left){
        if ((left.path && !left.sides[1]) || ((left == grid[0]) && (!this.sides[3]))) {
          line(centreX+w,centreY+w,x+w,y+(w/2)+w)
        }
      }
      if (right){
        if ((right.path && !right.sides[3]) || ((right == grid[grid.length-1]) && (!this.sides[1]))) {
          line(centreX+w,centreY+w,x+(w*2),y+(w/2)+w)
        }
      }
      if (bottom){
        if ((bottom.path && !bottom.sides[0]) || ((bottom == grid[grid.length-1]) && (!this.sides[2]))) {
          line(centreX+w,centreY+w,x+(w/2)+w,y+(w*2))
        }
      }
    }else if (this.blocked){//colours it red if blocked(marker)
        noStroke();
        fill(255,0,0,50)
        rect(x,y,w,w);
    }
    var x = (this.i-1)*w;
    var y = (this.j-1)*w;
    x = (this.i-1)*w;
    y = (this.j-1)*w;
    centreX = x+(w/2)
    centreY = y+(w/2)
    var top    = grid[index(i,j-1)];
    var right  = grid[index(i+1,j)];
    var bottom = grid[index(i,j+1)];
    var left   = grid[index(i-1,j)];//(w/3)/2
    if (this == grid[0]){
      if (right.path && !this.sides[1]){
        stroke(255,0,0,150);
        noFill();
        ellipse(centreX+w,centreY+w,w/3,w/3);
        line(centreX+w+(w/3)/2,centreY+w,x+(w*2),y+(w/2)+w)
      }
    }
    if (this == grid[0]){
      if (bottom.path && !this.sides[2]){
        stroke(255,0,0,150);
        noFill();
        ellipse(centreX+w,centreY+w,w/3,w/3);
        line(centreX+w,centreY+w+(w/3)/2,x+(w/2)+w,y+(w*2))
      }
    }
    if(this == grid[grid.length-1]){
      if (left.path && !this.sides[3]){
        stroke(255,0,0,150);
        noFill();
        ellipse(centreX+w,centreY+w,w/3,w/3);
        line(centreX+w-(w/3)/2,centreY+w,x+w,y+(w/2)+w)
      }
    }
    if(this == grid[grid.length-1]){
      if (top.path && !this.sides[0]){
        stroke(255,0,0,150);
        noFill();
        ellipse(centreX+w,centreY+w,w/3,w/3);
        line(centreX+w,centreY+w-(w/3)/2,x+(w/2)+w,y+w)
      }
    }
	}
  this.checkNeighbors = function(){//check if Neighbors havent been visited
    var neighbors = [];
    var top    = grid[index(i,j-1)];
    var right  = grid[index(i+1,j)];
    var bottom = grid[index(i,j+1)];
    var left   = grid[index(i-1,j)];

    if (top && !top.visited){
      neighbors.push(top);
    }
    if (right && !right.visited){
      neighbors.push(right);
    }
    if (bottom && !bottom.visited){
      neighbors.push(bottom);
    }
    if (left && !left.visited){
      neighbors.push(left);
    }

    if (neighbors.length > 0) {
      var r = floor(random(0, neighbors.length));
      return neighbors[r];
    }else{
      return undefined;
    }
  }
  this.checkNeighborsJunction = function(){//check if Neighbors havent been visited
    var neighbors = [];
    var top    = grid[index(this.i,this.j-1)];
    var right  = grid[index(this.i+1,this.j)];
    var bottom = grid[index(this.i,this.j+1)];
    var left   = grid[index(this.i-1,this.j)];

    if (top && !isJunction(top) && !this.sides[0] && !top.blocked && top != grid[grid.length-1]){//&& top!== grid[grid.length-1]){
      neighbors.push(top);
    }
    if (right && !isJunction(right) && !this.sides[1] && !right.blocked && right != grid[grid.length-1]){// && right !== grid[grid.length-1]){
      neighbors.push(right);
    }
    if (bottom && !isJunction(bottom) && !this.sides[2] && !bottom.blocked && bottom != grid[grid.length-1]){// && bottom !== grid[grid.length-1]){
      neighbors.push(bottom);
    }
    if (left && !isJunction(left) && !this.sides[3] && !left.blocked && left != grid[grid.length-1]){// && left !== grid[grid.length-1]){
      neighbors.push(left);
    }

    if (neighbors.length > 0) {
      var r = floor(random(0, neighbors.length));
      return neighbors[r];
    }else{
      return undefined;
    }
  }
  this.sideCountIncBlocked = function(){
    var count = 0;
    if(grid[index(this.i,this.j-1)]){//if top exists
      if (!this.sides[0] && !grid[index(this.i,this.j-1)].sides[2]){//if not got a wall between
        if(grid[index(this.i,this.j-1)].blocked){//if the cell is blocked
          count++//add to count
        }
      }
    }
    if(grid[index(this.i+1,this.j)]){//right
      if (!this.sides[1] && !grid[index(this.i+1,this.j)].sides[3]){
        if(grid[index(this.i+1,this.j)].blocked){
          count++
        }
      }
    }
    if(grid[index(this.i,this.j+1)]){//bottom
      if (!this.sides[2] && !grid[index(this.i,this.j+1)].sides[0]){
        if(grid[index(this.i,this.j+1)].blocked){
          count++
        }
      }
    }
    if(grid[index(this.i-1,this.j)]){//left
      if (!this.sides[3] && !grid[index(this.i-1,this.j)].sides[1]){
        if(grid[index(this.i-1,this.j)].blocked){
          count++
        }
      }
    }
    //sides works
    for (var j = 0; j < 4; j++){
      if(this.sides[j]){
        count++;
      }
    }
    //console.log(count)
    return count;
  }//returns number of sides that the current cell has
  this.sideCount = function(){
    var count = 0;
    for (var j = 0; j < 4; j++){
      if(this.sides[j]){
        count++;
      }
    }
    return count;
  }//returns number of sides that the current cell has
}























//whitespace
