<template>
	<div id="todo">
		<input
			type="text"
			v-model="searchText"
			placeholder="Search"
			clas="fixedElement"
		/>
		<form @submit.prevent="handleSubmitNewTask">
			<div class="tableFixHead">
				<h2 v-if="!submitValid" style="color: red">{{ invalidError }}</h2>
				<table class="table table-bordered mt-1 table">
					<thead>
						<tr>
							<th scope="col" style="width: 30%">Task</th>
							<th scope="col" style="width: 60%">Description</th>
							<th scope="col" style="width: 5%"></th>
						</tr>
					</thead>
					<tbody>
						<tr v-for="(task, index) in getterTodoList" :key="index">
							<template
								v-if="
									task.name
										.toLowerCase()
										.indexOf(searchText.toLowerCase()) >= 0 ||
									task.description
										.toLowerCase()
										.indexOf(searchText.toLowerCase()) >= 0
								"
							>
								<th>
									<span
										@click="taskMarkOff(index)"
										:class="{ taskDone: task.done }"
										>{{ task.name }}</span
									>
								</th>
								<th>
									<div @click="editDescription(index)">
										<span>{{ task.description }}&nbsp;</span>
									</div>
								</th>
								<th @click="deleteTask(index)">
									<div>
										<span class="fa fa-trash"></span>
									</div>
								</th>
							</template>
						</tr>
					</tbody>
				</table>
			</div>
			<table>
				<thead>
					<tr>
						<th scope="col" style="width: 30%">
							<input
								type="text"
								class="form-control"
								v-model="inputTask.name"
								placeholder="Enter task name"
								required
							/>
						</th>
						<th scope="col" style="width: 70%">
							<input
								type="text"
								class="form-control"
								v-model="inputTask.description"
								placeholder="Enter task description"
							/>
						</th>
					</tr>
				</thead>
			</table>
			<button class="mt-1 btn btn-primary btn-block">Submit</button>
		</form>
	</div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
	name: "TodoList",
	data() {
		return {
			inputTask: {
				name: "",
				description: "",
				done: false,
			},
			todoListData: [],
			submitValid: true,
			invalidError: "",
			searchText: "",
		};
	},
	methods: {
		async handleSubmitNewTask() {
			const exist = this.todoListData?.find(
				(task) => task.name === this.inputTask.name
			);
			if (exist) {
				this.invalidError = "Task already exist";
				this.submitValid = false;
				return;
			}
			this.submitValid = true;
			this.todoListData.push(JSON.parse(JSON.stringify(this.inputTask)));
			this.inputTask.name = "";
			this.inputTask.description = "";
		},
		taskMarkOff(index) {
			this.todoListData[index].done = !this.todoListData[index].done;
		},
		editDescription(index) {
			let newDesc = prompt(
				"Enter new description",
				this.todoListData[index].description
			);
			if (newDesc === null) return;
			this.todoListData[index].description = newDesc;
		},
		deleteTask(index) {
			this.todoListData.splice(index, 1);
		},
	},
	created() {
		this.todoListData = this.$store.getters.todoList;
	},
	watch: {
		todoListData: {
			handler() {
				if (!this.$store.getters.user) {
					this.$router.push("/login");
				}
				this.$store.dispatch("updateTodoList", this.todoListData);
			},
			deep: true,
		},
	},
	computed: {
		...mapGetters({
			getterTodoList: "todoList",
		}),
	},
};
</script>

<style>
.taskDone {
	text-decoration: line-through;
}
table {
	empty-cells: show;
	overflow-y: scroll;
}
.tableFixHead {
	overflow: auto;
	height: 400px;
}
.tableFixHead thead th {
	border: 1px solid #ddd;
	background-color: #f2f2f2;
	position: sticky;
	top: 0;
	z-index: 1;
}

/* Just common table stuff. Really. */
table {
	border-collapse: collapse;
	width: 100%;
}
</style>
