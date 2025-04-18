<!-- https://element-plus.org/zh-CN/component/form.html#%E5%85%B8%E5%9E%8B%E8%A1%A8%E5%8D%95 -->
<template>
	<div class="login-wrap">
		<div class="ms-login">
			<div class="ms-title">铁甲小记</div>
			<el-form :model="param" :rules="rules" ref="login" label-width="0px" class="ms-content">
				<el-form-item prop="username">
					<el-input v-model="param.username" placeholder="username">
						<template #prepend>
							<el-button :icon="User"></el-button>
						</template>
					</el-input>
				</el-form-item>
				<el-form-item prop="password">
					<el-input type="password" placeholder="password" v-model="param.password"
						@keyup.enter="submitForm(login)">
						<template #prepend>
							<el-button :icon="Lock"></el-button>
						</template>
					</el-input>
				</el-form-item>
				<div class="login-btn">
					<el-button type="primary" @click="submitForm(login)">登录</el-button>
				</div>
				<p class="login-tips">欢迎来到铁甲小记！</p>
			</el-form>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { useTagsStore } from '../store/tags';
import { usePermissStore } from '../store/permiss';
import { useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';
import type { FormInstance, FormRules } from 'element-plus';
import { Lock, User } from '@element-plus/icons-vue';
import service from '../utils/request';
import axios from 'axios';
interface LoginInfo {
	username: string;
	password: string;
}

const router = useRouter();
const param = reactive<LoginInfo>({
	username: 'Rosal1998',
	password: 'freedom1998.'
});

const rules: FormRules = {
	username: [
		{
			required: true,
			message: '请输入用户名',
			trigger: 'blur'
		}
	],
	password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
};
const permiss = usePermissStore();
const login = ref<FormInstance>();


// 登录函数定义
async function login1(username: string, password: string) {
	try {
		const response = await axios.get('http://127.0.0.1:5000/User/login', {
			params: {
				username, password
			}
		});
		console.log(response.data);
		return response.data; // 确保返回数据
	} catch (error) {
		console.log(error);
		throw error; // 抛出错误以便调用者捕获
	}
}

const submitForm = async (formEl: FormInstance | undefined) => {
	if (!formEl) return;
	formEl.validate(async (valid: boolean) => {
		if (valid) {
			try {
				let data = await login1(param.username, param.password);
				console.log(data);
				if (data === 'loginSuccess') {
					ElMessage.success('登录成功');
					localStorage.setItem('ms_username', param.username);
					console.log('param.username:', param.username)
					const keys = permiss.defaultList[param.username == 'Rosal1998' ? 'admin' : 'user'];
					console.log('permiss.defaultList:', permiss.defaultList)
					console.log('keys:', keys)
					permiss.handleSet(keys);
					localStorage.setItem('ms_keys', JSON.stringify(keys));
					router.push('/');
					console.log('-----router.push?-----')
				} else {
					// 处理登录失败的情况
					ElMessage.error('登录失败');
				}
			} catch (error) {
				// 如果login1抛出错误或者网络请求失败
				ElMessage.error('登录异常');
				console.error(error);
			}
		} else {
			ElMessage.error('请填写完整的表单');
		}
	});
};



const tags = useTagsStore();
tags.clearTags();
</script>

<style scoped>
.login-wrap {
	position: relative;
	width: 100%;
	height: 100%;
	background-image: url(../assets/img/bg.png);
	background-size: 100%;
}

.ms-title {
	width: 100%;
	line-height: 50px;
	text-align: center;
	font-size: 20px;
	color: #fff;
	border-bottom: 1px solid #ddd;
}

.ms-login {
	position: absolute;
	left: 50%;
	top: 50%;
	width: 350px;
	margin: -190px 0 0 -175px;
	border-radius: 5px;
	background: rgba(255, 255, 255, 0.3);
	overflow: hidden;
}

.ms-content {
	padding: 30px 30px;
}

.login-btn {
	text-align: center;
}

.login-btn button {
	width: 100%;
	height: 36px;
	margin-bottom: 10px;
}

.login-tips {
	font-size: 12px;
	line-height: 30px;
	color: #fff;
}
</style>
