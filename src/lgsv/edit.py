"""编辑题单相关功能"""
from lgsv import log, luogu


async def edit_training(
    training, add_problem=None, merge_training=None, remove_problem=None, problem_filter=None
):
    """编辑训练集，添加或合并题目"""
    await training.fetch_resources()
    if add_problem is not None:
        for p in add_problem:
            training.add_problem(p)
            log.logger.info("已向训练集 %s 添加题目 %s。", training.id, p)
    if merge_training is not None:
        for t in merge_training:
            training_obj = luogu.Training(training_id=t)
            await training_obj.fetch_resources()
            training.merge_training(training_obj)
            log.logger.info("已将训练集 %s 的题目合并至训练集 %s。", t, training.id)
    if remove_problem is not None:
        for p in remove_problem:
            training.remove_problem(p)
            log.logger.info("已从训练集 %s 移除题目 %s。", training.id, p)
    if problem_filter is not None:
        training.filt_by(problem_filter=problem_filter)
    await training.submit_changes()
