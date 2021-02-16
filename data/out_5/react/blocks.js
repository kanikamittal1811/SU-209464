import React from "react";
class Block1 extends React.Component{
	constructor(){
		super();
		this.state = {css:{
		block1:{
			clear:"left",
			marginBottom:"8px",
			border:"solid 2px black"
		},
		ul1:{
			float:"left"
		},
		li1:{
			float:"left",
			marginLeft:"203px"
		},
		div4:{
			width:"10px",
			marginLeft:"-406px",
			float:"left",
			height:"11px",
			background:"grey"
		},
		t0:{
			background:"green",
			height:"15px",
			width:"32px"
		},
		div6:{
			width:"167px",
			marginLeft:"140px",
			float:"left",
			height:"18px",
			background:"grey"
		},
		div5:{
			width:"39px",
			marginLeft:"4px",
			float:"left",
			height:"9px",
			background:"green"
		},
		div7:{
			width:"186px",
			marginLeft:"27px",
			float:"left",
			height:"18px",
			background:"grey"
		}
	}},
	render(){
		return (
			<div style={this.state.css.block1}>
				<ul style={this.state.css.ul1}>
					<li style={this.state.css.li1}>
						<div style={this.state.css.t0}>
						</div>
					</li>
					<li style={this.state.css.li1}>
						<div style={this.state.css.t0}>
						</div>
					</li>
					<li style={this.state.css.li1}>
						<div style={this.state.css.t0}>
						</div>
					</li>
				</ul>
				<div style={this.state.css.div4}>
				</div>
				<div style={this.state.css.div5}>
				</div>
				<div style={this.state.css.div6}>
				</div>
				<div style={this.state.css.div7}>
				</div>
			</div>
			
		)
	}
}

class Block2 extends React.Component{
	constructor(){
		super();
		this.state = {css:{
		li0:{
			float:"left",
			marginLeft:"15px"
		},
		ul0:{
			float:"left"
		},
		div12:{
			width:"101px",
			marginLeft:"455px",
			float:"left",
			height:"26px",
			background:"grey"
		},
		block2:{
			clear:"left",
			marginBottom:"14px",
			border:"solid 2px black"
		},
		nt16:{
			background:"grey",
			height:"26px",
			width:"54px"
		}
	}},
	render(){
		return (
			<div style={this.state.css.block2}>
				<ul style={this.state.css.ul0}>
					<li style={this.state.css.li0}>
						<div style={this.state.css.nt16}>
						</div>
					</li>
					<li style={this.state.css.li0}>
						<div style={this.state.css.nt16}>
						</div>
					</li>
				</ul>
				<div style={this.state.css.div12}>
				</div>
			</div>
			
		)
	}
}

class Block3 extends React.Component{
	constructor(){
		super();
		this.state = {css:{
		div14:{
			width:"9px",
			marginLeft:"-20px",
			float:"left",
			height:"88px",
			background:"orange"
		},
		div13:{
			width:"724px",
			float:"left",
			height:"136px",
			background:"grey"
		},
		block3:{
			clear:"left",
			marginBottom:"14px",
			border:"solid 2px black"
		}
	}},
	render(){
		return (
			<div style={this.state.css.block3}>
				<div style={this.state.css.div13}>
				</div>
				<div style={this.state.css.div14}>
				</div>
			</div>
			
		)
	}
}

export {Block1,Block2,Block3};