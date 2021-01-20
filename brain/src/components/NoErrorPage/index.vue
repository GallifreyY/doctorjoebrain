<template>
    <div style="background:#eee;padding: 20px">
        <Card :bordered="false">
            <p slot="title">{{$t("Congratulations!")}}</p>
            <p>{{$t("There is no peripheral issues found in your Horizon environment.")}}</p>
        </Card>
    </div>
</template>
<script>
    export default {
        name:'NoErrorPage',
    }
</script>
