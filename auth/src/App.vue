<template>
	<div id="app">
		<Nav />

		<div class="auth-wrapper">
			<div class="auth-inner">
				<router-view />
			</div>
		</div>
	</div>
</template>

<script>
import Nav from "./components/Nav.vue";
import axios from "axios";
export default {
	name: "App",
	components: {
		Nav,
	},
	async created() {
		const response = await axios.get("user").catch(() => {
			this.$router.push("/login");
		});
		if (response?.data?.status !== "success") {
			this.$router.push("/login");
		} else {
			console.log(response);
			await this.$store.dispatch("user", response?.data);
			await this.$store.dispatch("todoList", response?.data.tasks);
		}
	},
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;500;600;700&display=swap");
* {
	font: sans-serif;
	box-sizing: border-box;
}
body {
	background-color: #5665a6;
	min-height: 100vh;
	display: flex;
}
nav {
	background-color: #f3f3f3;
}
body,
html,
#app,
#root,
.auth-wrapper {
	width: 100%;
	height: 100%;
}
#app {
	text-align: center;
}
.auth-wrapper {
	display: flex;
	justify-content: center;
	flex-direction: column;
	text-align: left;
}
.auth-inner {
	max-height: 80%;
	width: 600px;
	margin: auto;
	background-color: #fff;
	box-shadow: 0px 14px 80px #ccc rgba(0, 0, 0, 0.5);
	padding: 20px;
	border-radius: 15px;
	overflow: scroll;
}
.auth-wrapper .form-control:focus {
	box-shadow: none;
}
.auth-wrapper h3 {
	text-align: center;
	margin: 0;
	line-height: 1;
	padding-bottom: 20px;
}
.custom-control-label::before {
	font-weight: 400;
}
</style>
