<template>
	<div>
		<el-row :gutter="20">
			<el-col :span="8" v-for="(item, index) in knowledge"
				@click="GotoDetail(item.knowledgeId, item.knowledgeName)" :key="index">
				<el-card shadow="hover">
					<template #header>
						<div class="clearfix">
							<h3>{{ item.knowledgeName }}</h3>
						</div>
					</template>
					<span>{{ item.description }}</span>
				</el-card>
			</el-col>
			<el-col :span="8">
				<el-card shadow="hover" style="text-align: center;">
					<el-button type="success" :icon="Plus" @click="dialogFormVisible = true" circle />
				</el-card>
			</el-col>
		</el-row>

		<el-row>
			<el-col :span="10" :offset="7">
				<el-dialog width="30%" v-model="dialogFormVisible" title="添加知识库" align-center>
					<el-form :model="form">
						<el-form-item label="知识库名" label-width="auto" style="max-width: 500px">
							<el-input v-model="form.name" autocomplete="off" />
						</el-form-item>
						<el-form-item label="知识库描述" label-width="auto" style="max-width: 500px">
							<el-input v-model="form.description" autocomplete="off" />
						</el-form-item>
					</el-form>

					<template #footer>
						<div class="dialog-footer">
							<el-button @click="dialogFormVisible = false">取消</el-button>
							<el-button type="primary" @click="submitKnowledge">
								确定
							</el-button>
						</div>
					</template>
				</el-dialog>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="workStage">
import {
	Plus
} from '@element-plus/icons-vue'

import { ref, reactive } from 'vue'
import imgurl from '../assets/img/img.jpg';
const id = 'preview-only';
const text = ref('# Hello Editor');
import  MdPreview from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import axios from 'axios';
import router from '../router';
const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';
const knowledge: any = ref([]);
const dialogFormVisible = ref(false)
const form = reactive({
	name: '',
	description:''
})
const getKnowledge = () => {
	console.log('【拉取知识库】')
	axios.get('http://127.0.0.1:5000/Knowledge/showInfo', {
		params: {
			userId: name
		}
	})
		.then(function (response) {
			knowledge.value = response.data;
			console.log(knowledge.value)
		})
		.catch(function (error) {
			console.log(error);
		});
}
const submitKnowledge = () => {
	console.log('【添加知识库】')
	axios.get('http://127.0.0.1:5000/Knowledge/add', {
		params: {
			userId: name,
			knowledgeName: form.name,
			description:form.description
		}
	})
		.then(function (response) {
			dialogFormVisible.value = false
			getKnowledge();
		})
		.catch(function (error) {
			console.log(error);
		});
}
const GotoDetail = (knowledgeId: string, knowledgeName: string) => {
	console.log(knowledgeId)
	router.push({
		name: 'textEditor',
		params: {
			knowledgeId: knowledgeId,
			knowledgeName: knowledgeName
		} // 确保传递knowledgeId而不是'1'
	});
}
getKnowledge();
</script>

<style scoped>
.el-row {
	margin-bottom: 20px;
}

.grid-content {
	display: flex;
	align-items: center;
	height: 100px;
}

.grid-cont-right {
	flex: 1;
	text-align: center;
	font-size: 14px;
	color: #999;
}

.grid-num {
	font-size: 30px;
	font-weight: bold;
}

.grid-con-icon {
	font-size: 50px;
	width: 100px;
	height: 100px;
	text-align: center;
	line-height: 100px;
	color: #fff;
}

.grid-con-1 .grid-con-icon {
	background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
	color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
	background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
	color: rgb(100, 213, 114);
}

.grid-con-3 .grid-con-icon {
	background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
	color: rgb(242, 94, 67);
}

.user-info {
	display: flex;
	align-items: center;
	padding-bottom: 20px;
}

.user-info-cont {
	padding-left: 50px;
	flex: 1;
	font-size: 14px;
	color: #999;
}

.user-info-cont div:first-child {
	font-size: 30px;
	color: #222;
}

.user-info-list {
	font-size: 14px;
	color: #999;
	line-height: 25px;
}

.user-info-list span {
	margin-left: 70px;
}

.contribution-day {
	width: 30px;
	height: 30px;
	background-color: #ebedf0;
	border-radius: 2px;
	outline: 1px solid #dee0e3;
	outline-offset: -1px;
	text-align: center;
	line-height: 30px;
	font-weight: 100;
}

.contribution-card {
	margin: 2px;
	padding: 0px;
}

.el-dialog {
	width: 30%;
}
</style>
