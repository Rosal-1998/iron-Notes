<template>
	<div>
		<!-- <div class="container"> -->
		<div class="plugins-tips">
			<h1>{{knowledgeName}}</h1>
		</div>
		<md-editor class="mgb20" v-model="knowledgeDetail" @on-upload-img="onUploadImg" />
		<el-button type="primary" @click="submitKnowDetail">提交</el-button>
		<!-- </div> -->
	</div>

</template>

<script setup lang="ts" name="textEditor">
import { ref } from 'vue';
import MdEditor from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import router from '../router';
import { useRoute } from 'vue-router';
import axios from 'axios';
const route = useRoute();
const knowledgeName = route.params.knowledgeName; // 使用data变量接收参数
const knowledgeId = route.params.knowledgeId; // 使用data变量接收参数
const knowledgeDetail: any = ref('');
// const text = ref('Hello Editor!');
const onUploadImg = (files: any) => {
	console.log(files);
};
console.log('---?---')
const init = () => {
	console.log('----编辑页面----')
	axios.get('http://127.0.0.1:5000/Knowledge/showDetail', {
		params: {
			knowledgeId: knowledgeId
		}
	})
		.then(function (response) {
			knowledgeDetail.value = response.data[0].detail;
		})
		.catch(function (error) {
			console.log(error);
		});
}
const submitKnowDetail = () =>{
	console.log(knowledgeDetail)
	console.log('----提交详情----')
	axios.get('http://127.0.0.1:5000/Knowledge/updateDetail', {
		params: {
			knowledgeId: knowledgeId,
			detail:knowledgeDetail.value
		}
	})
		.then(function (response) {
			console.log(response.data)
			init();
		})
		.catch(function (error) {
			console.log(error);
		});
}
init();
</script>
