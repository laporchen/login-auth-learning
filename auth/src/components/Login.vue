<template>
	<div id="login">
		<form @submit.prevent="handleLogin">
			<h3>Login</h3>
			<div class="form-group">
				<label>Email</label>
				<input
					type="email"
					class="form-control"
					v-model="email"
					placeholder="Enter email"
				/>
			</div>
			<div class="form-group">
				<label>Password</label>
				<input
					type="password"
					class="form-control"
					v-model="passowrd"
					placeholder="Enter password"
				/>
			</div>
			<button class="mt-1 btn btn-primary btn-block">Login</button>
		</form>
	</div>
</template>

<script>
import axios from "axios";
export default {
	name: "Login",
	data() {
		return {
			user: {
				email: "",
				password: "",
			},
		};
	},
	methods: {
		async handleLogin() {
			const loginUser = {
				email: this.user.email,
				password: this.user.password,
			};
			const response = await axios.post("login", loginUser);
			if (response?.data?.status !== "success") {
				alert("Email or password is incorrect");
				return;
			} else {
				this.$router.push("/home");
			}
		},
	},
};
</script>
