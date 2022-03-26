<template>
	<div id="nav">
		<nav class="navbar navbar-expand navbar-light fixed-top">
			<div class="container">
				<router-link v-if="user" class="navbar-brand" to="/"
					>Hello, {{ user?.name }}</router-link
				>
				<router-link v-else class="navbar-brand" to="/">Login first</router-link>
				<div class="collapse navbar-collapse">
					<ul v-if="!user" class="navbar-nav ms-auto">
						<li class="nav-item">
							<router-link to="/login" class="nav-link">Login</router-link>
						</li>
						<li class="nav-item">
							<router-link to="/register" class="nav-link"
								>Register</router-link
							>
						</li>
					</ul>
					<ul v-if="user" class="navbar-nav ms-auto">
						<li class="nav-item">
							<router-link
								to="/login"
								class="nav-link"
								@click="logoutHandle"
								>Logout</router-link
							>
						</li>
					</ul>
				</div>
			</div>
		</nav>
	</div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
	name: "Nav",
	methods: {
		logoutHandle() {
			localStorage.removeItem("token");
			this.$store.dispatch("user", null);
			this.$router.push("/login");
		},
	},
	computed: {
		...mapGetters(["user"]),
	},
};
</script>
