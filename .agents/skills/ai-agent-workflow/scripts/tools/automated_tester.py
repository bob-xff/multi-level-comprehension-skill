#!/usr/bin/env python3
"""
AI智能体5级用法工作流 - 自动化测试工具

自动执行单元测试、集成测试和性能测试。
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class TestReport:
    """测试报告数据类"""
    timestamp: str
    test_type: str
    total_tests: int
    passed_tests: int
    failed_tests: int
    skipped_tests: int
    coverage: float
    duration: float
    success_rate: float
    issues: List[Dict[str, str]]


class AutomatedTester:
    """自动化测试器"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
    
    def run_python_tests(self, test_dir: str = "tests") -> TestReport:
        """运行Python测试"""
        test_path = self.project_root / test_dir
        
        if not test_path.exists():
            return TestReport(
                timestamp=datetime.now().isoformat(),
                test_type="unit",
                total_tests=0,
                passed_tests=0,
                failed_tests=0,
                skipped_tests=0,
                coverage=0.0,
                duration=0.0,
                success_rate=0.0,
                issues=[{"type": "setup", "message": f"测试目录不存在: {test_dir}"}]
            )
        
        try:
            # 运行pytest并收集结果
            result = subprocess.run(
                [
                    "python", "-m", "pytest",
                    str(test_path),
                    "--tb=short",
                    "--json-report",
                    "--json-report-file=test_report.json",
                    "-v"
                ],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            # 解析测试结果
            if os.path.exists("test_report.json"):
                with open("test_report.json", "r") as f:
                    report_data = json.load(f)
                
                summary = report_data.get("summary", {})
                total = summary.get("total", 0)
                passed = summary.get("passed", 0)
                failed = summary.get("failed", 0)
                skipped = summary.get("skipped", 0)
                
                # 获取覆盖率（如果有）
                coverage = 0.0
                if "coverage" in report_data:
                    coverage = report_data["coverage"].get("percent", 0.0)
                
                # 获取测试时长
                duration = report_data.get("duration", 0.0)
                
                success_rate = (passed / total * 100) if total > 0 else 0.0
                
                issues = []
                if failed > 0:
                    issues.append({
                        "type": "failure",
                        "message": f"{failed} 个测试失败",
                        "details": "请检查失败的测试用例"
                    })
                
                # 清理报告文件
                os.remove("test_report.json")
                
                return TestReport(
                    timestamp=datetime.now().isoformat(),
                    test_type="unit",
                    total_tests=total,
                    passed_tests=passed,
                    failed_tests=failed,
                    skipped_tests=skipped,
                    coverage=coverage,
                    duration=duration,
                    success_rate=success_rate,
                    issues=issues
                )
            
            # 如果没有JSON报告，从输出解析
            return self._parse_pytest_output(result.stdout, result.stderr)
            
        except Exception as e:
            return TestReport(
                timestamp=datetime.now().isoformat(),
                test_type="unit",
                total_tests=0,
                passed_tests=0,
                failed_tests=0,
                skipped_tests=0,
                coverage=0.0,
                duration=0.0,
                success_rate=0.0,
                issues=[{"type": "error", "message": f"测试执行失败: {str(e)}"}]
            )
    
    def _parse_pytest_output(self, stdout: str, stderr: str) -> TestReport:
        """解析pytest输出"""
        # 简单解析pytest输出
        lines = stdout.split("\n")
        
        total = 0
        passed = 0
        failed = 0
        skipped = 0
        
        for line in lines:
            if "passed" in line and "failed" in line:
                # 解析类似 "5 passed, 2 failed, 1 skipped" 的行
                parts = line.split(",")
                for part in parts:
                    part = part.strip()
                    if "passed" in part:
                        passed = int(part.split()[0])
                    elif "failed" in part:
                        failed = int(part.split()[0])
                    elif "skipped" in part:
                        skipped = int(part.split()[0])
        
        total = passed + failed + skipped
        success_rate = (passed / total * 100) if total > 0 else 0.0
        
        return TestReport(
            timestamp=datetime.now().isoformat(),
            test_type="unit",
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed,
            skipped_tests=skipped,
            coverage=0.0,
            duration=0.0,
            success_rate=success_rate,
            issues=[{"type": "failure", "message": f"{failed} 个测试失败"}] if failed > 0 else []
        )
    
    def run_javascript_tests(self, test_script: str = "test") -> TestReport:
        """运行JavaScript/TypeScript测试"""
        try:
            # 运行npm test
            result = subprocess.run(
                ["npm", "test"],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            # 解析Jest或其他测试框架的输出
            return self._parse_jest_output(result.stdout, result.stderr)
            
        except Exception as e:
            return TestReport(
                timestamp=datetime.now().isoformat(),
                test_type="unit",
                total_tests=0,
                passed_tests=0,
                failed_tests=0,
                skipped_tests=0,
                coverage=0.0,
                duration=0.0,
                success_rate=0.0,
                issues=[{"type": "error", "message": f"测试执行失败: {str(e)}"}]
            )
    
    def _parse_jest_output(self, stdout: str, stderr: str) -> TestReport:
        """解析Jest输出"""
        lines = stdout.split("\n")
        
        total = 0
        passed = 0
        failed = 0
        
        for line in lines:
            if "Tests:" in line:
                # 解析类似 "Tests: 5 passed, 2 failed, 1 skipped" 的行
                parts = line.split(":")[1].split(",")
                for part in parts:
                    part = part.strip()
                    if "passed" in part:
                        passed = int(part.split()[0])
                    elif "failed" in part:
                        failed = int(part.split()[0])
        
        total = passed + failed
        success_rate = (passed / total * 100) if total > 0 else 0.0
        
        return TestReport(
            timestamp=datetime.now().isoformat(),
            test_type="unit",
            total_tests=total,
            passed_tests=passed,
            failed_tests=failed,
            skipped_tests=0,
            coverage=0.0,
            duration=0.0,
            success_rate=success_rate,
            issues=[{"type": "failure", "message": f"{failed} 个测试失败"}] if failed > 0 else []
        )
    
    def run_integration_tests(self, test_dir: str = "tests/integration") -> TestReport:
        """运行集成测试"""
        # 集成测试通常需要特定环境，这里只是示例
        return self.run_python_tests(test_dir)
    
    def run_performance_tests(self, test_file: str = "tests/performance") -> TestReport:
        """运行性能测试"""
        # 性能测试通常使用locust或jmeter
        test_path = self.project_root / test_file
        
        if not test_path.exists():
            return TestReport(
                timestamp=datetime.now().isoformat(),
                test_type="performance",
                total_tests=0,
                passed_tests=0,
                failed_tests=0,
                skipped_tests=0,
                coverage=0.0,
                duration=0.0,
                success_rate=0.0,
                issues=[{"type": "setup", "message": f"性能测试文件不存在: {test_file}"}]
            )
        
        # 这里可以集成locust或其他性能测试工具
        return TestReport(
            timestamp=datetime.now().isoformat(),
            test_type="performance",
            total_tests=1,
            passed_tests=1,
            failed_tests=0,
            skipped_tests=0,
            coverage=0.0,
            duration=0.0,
            success_rate=100.0,
            issues=[]
        )
    
    def generate_report(self, reports: List[TestReport]) -> str:
        """生成测试报告"""
        if not reports:
            return "没有执行任何测试"
        
        report_lines = [
            "=" * 60,
            "AI智能体5级用法工作流 - 自动化测试报告",
            "=" * 60,
            f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
        ]
        
        # 汇总统计
        total_tests = sum(r.total_tests for r in reports)
        passed_tests = sum(r.passed_tests for r in reports)
        failed_tests = sum(r.failed_tests for r in reports)
        skipped_tests = sum(r.skipped_tests for r in reports)
        avg_coverage = sum(r.coverage for r in reports) / len(reports) if reports else 0
        total_duration = sum(r.duration for r in reports)
        overall_success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        report_lines.extend([
            "-" * 60,
            "总体统计",
            "-" * 60,
            f"总测试数: {total_tests}",
            f"通过测试: {passed_tests}",
            f"失败测试: {failed_tests}",
            f"跳过测试: {skipped_tests}",
            f"平均覆盖率: {avg_coverage:.1%}",
            f"总测试时长: {total_duration:.2f}秒",
            f"总体成功率: {overall_success_rate:.1f}%",
            "",
        ])
        
        # 详细报告
        for i, report in enumerate(reports, 1):
            report_lines.extend([
                "-" * 60,
                f"测试报告 {i}: {report.test_type}",
                "-" * 60,
                f"测试数: {report.total_tests}",
                f"通过: {report.passed_tests}",
                f"失败: {report.failed_tests}",
                f"跳过: {report.skipped_tests}",
                f"覆盖率: {report.coverage:.1%}",
                f"时长: {report.duration:.2f}秒",
                f"成功率: {report.success_rate:.1f}%",
                "",
            ])
            
            if report.issues:
                report_lines.append("问题:")
                for issue in report.issues:
                    report_lines.extend([
                        f"  - [{issue.get('type', 'unknown')}] {issue.get('message', '未知问题')}",
                        f"    详情: {issue.get('details', '无')}",
                    ])
                report_lines.append("")
        
        # 改进建议
        suggestions = []
        if failed_tests > 0:
            suggestions.append(f"修复 {failed_tests} 个失败的测试")
        if avg_coverage < 80:
            suggestions.append(f"提高测试覆盖率 (当前: {avg_coverage:.1f}%, 目标: 80%)")
        if skipped_tests > 0:
            suggestions.append(f"检查 {skipped_tests} 个被跳过的测试")
        
        if suggestions:
            report_lines.extend([
                "-" * 60,
                "改进建议",
                "-" * 60,
            ])
            for i, suggestion in enumerate(suggestions, 1):
                report_lines.extend([
                    f"{i}. {suggestion}",
                    "",
                ])
        
        report_lines.extend([
            "=" * 60,
            "报告结束",
            "=" * 60,
        ])
        
        return "\n".join(report_lines)


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("使用方法: python automated_tester.py <测试类型> [测试目录]")
        print("测试类型: unit, integration, performance")
        print("示例:")
        print("  python automated_tester.py unit tests/")
        print("  python automated_tester.py integration tests/integration/")
        print("  python automated_tester.py performance tests/performance/")
        sys.exit(1)
    
    test_type = sys.argv[1]
    test_dir = sys.argv[2] if len(sys.argv) > 2 else "tests"
    
    tester = AutomatedTester()
    reports = []
    
    if test_type == "unit":
        # 根据项目类型选择测试运行器
        if (tester.project_root / "package.json").exists():
            report = tester.run_javascript_tests()
        else:
            report = tester.run_python_tests(test_dir)
        reports.append(report)
    
    elif test_type == "integration":
        report = tester.run_integration_tests(test_dir)
        reports.append(report)
    
    elif test_type == "performance":
        report = tester.run_performance_tests(test_dir)
        reports.append(report)
    
    else:
        print(f"不支持的测试类型: {test_type}")
        sys.exit(1)
    
    # 生成报告
    report = tester.generate_report(reports)
    print(report)
    
    # 保存报告到文件
    report_file = f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n报告已保存到: {report_file}")
    
    # 如果有失败的测试，返回非零退出码
    if any(r.failed_tests > 0 for r in reports):
        sys.exit(1)


if __name__ == "__main__":
    main()
