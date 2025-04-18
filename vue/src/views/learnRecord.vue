<template>
	<div>
		<el-row :gutter="20">
			<el-col :span="10">
				<el-card shadow="hover" class="mgb20">
					<div class="user-info">
						<el-avatar :size="120" :src="imgurl" />
						<div class="user-info-cont">
							<div class="user-info-name">{{ name }}</div>
							<div style="margin-top: 10px;">TaylorSwift Role the World!!!</div>
						</div>
					</div>
					<el-card shadow="always">
						<template #header>
							<div class="card-header">
								<span>本月学习贡献</span>
							</div>
						</template>
						<el-row :gutter="12" style="margin-left: 20px;">
							<el-col :span="2" v-for="o in Number(yearMonthDays.toString().slice(4, 6))" :key="o"
								class="contribution-card" style="padding: 3px;">
								<div class="contribution-day" :style="getContributionsStyle(o)">
									<span style="font-weight: 100;">{{ o }}</span>
								</div>
							</el-col>
						</el-row>
					</el-card>
				</el-card>
				<el-card shadow="hover">

					<template #header>
						<div class="clearfix">
							<span>学习日报</span>
						</div>
					</template>
					<el-timeline>
						<el-timeline-item v-for="(record, index) in learnRecords" :key="index"
							:timestamp=timestampToDateTime(record.learnrecordid) placement="top">
							<el-card>
								<el-row>
									<el-col :span="22">
										<h3>{{ record.learnrecordcontent }}</h3>
									</el-col>
									<el-col :span="2">
										<el-button type="danger" :icon="Delete"
											@click='deleteLearnRecord(record.learnrecordid)' circle />
									</el-col>
								</el-row>
							</el-card>
						</el-timeline-item>
					</el-timeline>

				</el-card>
			</el-col>
			<el-col :span="14">
				<el-card shadow="hover" style="height: 403px">

					<template #header>
						<div class="clearfix">
							<span>小记</span>
						</div>
					</template>
					<el-input v-model="learnRecordEditor" :rows="10" type="textarea" placeholder="记录今天所学...." />
					<el-button type="success" @click='sumbitLearnRecord' style="margin-top: 10px;" plain
						:disabled="learnRecordEditor.length < 1">提交</el-button>
				</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="learnRecord">
// import { reactive } from 'vue';
import {
	Delete,
} from '@element-plus/icons-vue'
import { ref } from 'vue'
import imgurl from '../assets/img/img.jpg';
import axios from 'axios';
const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';
// const ref:any = useRef(null)
const learnRecords: any = ref([]);
const learnRecordEditor = ref('')
// const days = ref();
const yearMonthDays = ref();
const contributions: any = ref([]);

const getlearnRecord = () => {
	console.log('【拉取学习记录】')
	axios.get('http://127.0.0.1:5000/LearnRecord/showInfo', {
		params: {
			userId: name
		}
	})
		.then(function (response) {
			learnRecords.value = response.data.reverse();
		})
		.catch(function (error) {
			console.log(error);
		});
}
const sumbitLearnRecord = () => {
	console.log('【提交学习记录】')
	const timeStamp = Math.floor(new Date().getTime() / 1000);
	console.log()
	axios.get('http://127.0.0.1:5000/LearnRecord/add', {
		params: {
			userId: name,
			content: learnRecordEditor.value,
			time: timeStamp
		}
	})
		.then(function (response) {
			getlearnRecord();
			getContributions();
			learnRecordEditor.value = ''
		})
		.catch(function (error) {
			console.log(error);
		});

}
const timestampToDateTime = (timestamp: number) => {
	// 创建一个新的Date对象，将时间戳作为参数传递
	var date = new Date(timestamp * 1000);
	var year = date.getFullYear();
	var month = ('0' + (date.getMonth() + 1)).slice(-2);
	var day = ('0' + date.getDate()).slice(-2);
	var hours = ('0' + date.getHours()).slice(-2);
	var minutes = ('0' + date.getMinutes()).slice(-2);
	var seconds = ('0' + date.getSeconds()).slice(-2);
	return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds;
}
const deleteLearnRecord = (event: string) => {
	console.log('【删除学习记录】')
	axios.get('http://127.0.0.1:5000/LearnRecord/delete', {
		params: {
			learnrecordid: event
		}
	})
		.then(function (response) {
			getlearnRecord();
		})
		.catch(function (error) {
			console.log(error);
		});
}
const initContributions = () => {
	const now = new Date(); // 获取当前日期
	const year = now.getFullYear(); // 当前年份
	const month = now.getMonth() + 1; // 当前月份（注意：0表示一月，11表示十二月）
	const day = new Date(year, month, 0).getDate(); // 获取当前月份的天数
	// days.value = day
	// 编码为现在的年-月
	yearMonthDays.value = year.toString().slice(2, 4) + ((month < 10) ? '0' + month.toString() : month.toString()) + day.toString()
}

const getContributions = () => {
	console.log('【拉取贡献】')
	axios.get('http://127.0.0.1:5000/Contributions/showInfo', {
		params: {
			userId: name,
			date: (yearMonthDays.value).toString().slice(0, 4)
		}
	})
		.then(function (response) {
			console.log(response.data)
			contributions.value = response.data
		})
		.catch(function (error) {
			console.log(error);
		});
}

const getContributionsStyle = (day: number) => {
	const Cday = contributions.value.find(contributions => Number(contributions.date.toString().slice(4, 6)) === day);
	if (Cday) {
		if (Cday["times"] > 2) {
			return 'background-color: #529b2e';
		} else if (Cday["times"] > 1) {
			return 'background-color: #b3e19d';
		}
		else {
			return 'background-color: #e1f3d8';
		}
	}
	return ''
}

getlearnRecord();
initContributions();
getContributions();
console.log(yearMonthDays.value)
console.log(yearMonthDays.value.toString().slice(4, 6))
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
</style>
