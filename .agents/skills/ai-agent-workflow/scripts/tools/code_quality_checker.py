#!/usr/bin/env python3
"""
AI智能体5级用法工作流 - 代码质量检查工具

自动执行代码格式检查、安全扫描和质量评估。
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
class QualityReport:
    """质量报告数据类"""
    timestamp: str
    file_path: str
    format_score: float
    security_score: float
    quality_score: float
    overall_score: float
    issues: List[Dict[str, str]]
    suggestions: List[str]


class CodeQualityChecker:
    """代码质量检查器"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.results = []
    
    def check_python_code(self, file_path: str) -> QualityReport:
        """检查Python代码质量"""
        issues = []
        suggestions = []
        
        # 1. 格式检查 (使用black)
        format_score = self._check_format(file_path, issues, suggestions)
        
        # 2. 安全检查 (使用bandit)
        security_score = self._check_security(file_path, issues, suggestions)
        
        # 3. 质量检查 (使用pylint)
        quality_score = self._check_quality(file_path, issues, suggestions)
        
        # 计算总分
        overall_score = (format_score + security_score + quality_score) / 3
        
        return QualityReport(
            timestamp=datetime.now().isoformat(),
            file_path=file_path,
            format_score=format_score,
            security_score=security_score,
            quality_score=quality_score,
            overall_score=overall_score,
            issues=issues,
            suggestions=suggestions
        )
    
    def _check_format(self, file_path: str, issues: List, suggestions: List) -> float:
        """检查代码格式"""
        try:
            # 使用black检查格式
            result = subprocess.run(
                ["python", "-m", "black", "--check", "--diff", file_path],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            if result.returncode != 0:
                issues.append({
                    "type": "format",
                    "severity": "warning",
                    "message": "代码格式不符合规范",
                    "details": result.stdout[:500] if result.stdout else "格式问题"
                })
                suggestions.append("运行 'black .' 自动格式化代码")
                return 0.7
            
            return 1.0
            
        except FileNotFoundError:
            issues.append({
                "type": "format",
                "severity": "info",
                "message": "未安装black格式化工具",
                "details": "请运行 'pip install black' 安装"
            })
            suggestions.append("安装black: pip install black")
            return 0.5
    
    def _check_security(self, file_path: str, issues: List, suggestions: List) -> float:
        """检查代码安全"""
        try:
            # 使用bandit检查安全问题
            result = subprocess.run(
                ["python", "-m", "bandit", "-r", file_path, "-f", "json"],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            if result.stdout:
                bandit_results = json.loads(result.stdout)
                high_severity = len([r for r in bandit_results.get("results", []) 
                                   if r.get("issue_severity") == "HIGH"])
                medium_severity = len([r for r in bandit_results.get("results", []) 
                                     if r.get("issue_severity") == "MEDIUM"])
                
                if high_severity > 0:
                    issues.append({
                        "type": "security",
                        "severity": "high",
                        "message": f"发现 {high_severity} 个高风险安全问题",
                        "details": "请立即修复安全漏洞"
                    })
                    suggestions.append("修复高风险安全漏洞")
                    return 0.3
                
                if medium_severity > 0:
                    issues.append({
                        "type": "security",
                        "severity": "medium",
                        "message": f"发现 {medium_severity} 个中等风险安全问题",
                        "details": "建议修复安全问题"
                    })
                    suggestions.append("修复中等风险安全问题")
                    return 0.6
            
            return 1.0
            
        except FileNotFoundError:
            issues.append({
                "type": "security",
                "severity": "info",
                "message": "未安装bandit安全检查工具",
                "details": "请运行 'pip install bandit' 安装"
            })
            suggestions.append("安装bandit: pip install bandit")
            return 0.5
    
    def _check_quality(self, file_path: str, issues: List, suggestions: List) -> float:
        """检查代码质量"""
        try:
            # 使用pylint检查代码质量
            result = subprocess.run(
                ["python", "-m", "pylint", "--output-format=json", file_path],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            if result.stdout:
                pylint_results = json.loads(result.stdout)
                errors = len([r for r in pylint_results if r.get("type") == "error"])
                warnings = len([r for r in pylint_results if r.get("type") == "warning"])
                refactor = len([r for r in pylint_results if r.get("type") == "refactor"])
                
                if errors > 0:
                    issues.append({
                        "type": "quality",
                        "severity": "high",
                        "message": f"发现 {errors} 个代码错误",
                        "details": "必须修复代码错误"
                    })
                    suggestions.append("修复代码错误")
                    return 0.4
                
                if warnings > 0:
                    issues.append({
                        "type": "quality",
                        "severity": "medium",
                        "message": f"发现 {warnings} 个代码警告",
                        "details": "建议修复代码警告"
                    })
                    suggestions.append("修复代码警告")
                    return 0.7
                
                if refactor > 0:
                    suggestions.append("考虑重构代码以提高可读性")
                    return 0.9
            
            return 1.0
            
        except FileNotFoundError:
            issues.append({
                "type": "quality",
                "severity": "info",
                "message": "未安装pylint质量检查工具",
                "details": "请运行 'pip install pylint' 安装"
            })
            suggestions.append("安装pylint: pip install pylint")
            return 0.5
    
    def check_javascript_code(self, file_path: str) -> QualityReport:
        """检查JavaScript/TypeScript代码质量"""
        issues = []
        suggestions = []
        
        # 1. 格式检查 (使用prettier)
        format_score = self._check_js_format(file_path, issues, suggestions)
        
        # 2. 安全检查 (使用npm audit)
        security_score = self._check_js_security(file_path, issues, suggestions)
        
        # 3. 质量检查 (使用eslint)
        quality_score = self._check_js_quality(file_path, issues, suggestions)
        
        # 计算总分
        overall_score = (format_score + security_score + quality_score) / 3
        
        return QualityReport(
            timestamp=datetime.now().isoformat(),
            file_path=file_path,
            format_score=format_score,
            security_score=security_score,
            quality_score=quality_score,
            overall_score=overall_score,
            issues=issues,
            suggestions=suggestions
        )
    
    def _check_js_format(self, file_path: str, issues: List, suggestions: List) -> float:
        """检查JavaScript格式"""
        try:
            result = subprocess.run(
                ["npx", "prettier", "--check", file_path],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            if result.returncode != 0:
                issues.append({
                    "type": "format",
                    "severity": "warning",
                    "message": "代码格式不符合规范",
                    "details": "请运行prettier格式化"
                })
                suggestions.append("运行 'npx prettier --write .' 自动格式化")
                return 0.7
            
            return 1.0
            
        except FileNotFoundError:
            suggestions.append("安装prettier: npm install -g prettier")
            return 0.5
    
    def _check_js_security(self, file_path: str, issues: List, suggestions: List) -> float:
        """检查JavaScript安全"""
        try:
            result = subprocess.run(
                ["npm", "audit", "--json"],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            if result.stdout:
                audit_results = json.loads(result.stdout)
                vulnerabilities = audit_results.get("vulnerabilities", {})
                
                high_vulns = sum(1 for v in vulnerabilities.values() 
                               if v.get("severity") == "high")
                
                if high_vulns > 0:
                    issues.append({
                        "type": "security",
                        "severity": "high",
                        "message": f"发现 {high_vulns} 个高风险漏洞",
                        "details": "请立即更新依赖"
                    })
                    suggestions.append("运行 'npm audit fix' 修复漏洞")
                    return 0.3
            
            return 1.0
            
        except FileNotFoundError:
            suggestions.append("确保已安装npm")
            return 0.5
    
    def _check_js_quality(self, file_path: str, issues: List, suggestions: List) -> float:
        """检查JavaScript质量"""
        try:
            result = subprocess.run(
                ["npx", "eslint", file_path],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            if result.returncode != 0:
                error_count = result.stdout.count("error")
                warning_count = result.stdout.count("warning")
                
                if error_count > 0:
                    issues.append({
                        "type": "quality",
                        "severity": "high",
                        "message": f"发现 {error_count} 个ESLint错误",
                        "details": "必须修复ESLint错误"
                    })
                    suggestions.append("修复ESLint错误")
                    return 0.4
                
                if warning_count > 0:
                    issues.append({
                        "type": "quality",
                        "severity": "medium",
                        "message": f"发现 {warning_count} 个ESLint警告",
                        "details": "建议修复ESLint警告"
                    })
                    suggestions.append("修复ESLint警告")
                    return 0.7
            
            return 1.0
            
        except FileNotFoundError:
            suggestions.append("安装ESLint: npm install -g eslint")
            return 0.5
    
    def generate_report(self, reports: List[QualityReport]) -> str:
        """生成质量报告"""
        if not reports:
            return "没有可检查的文件"
        
        report_lines = [
            "=" * 60,
            "AI智能体5级用法工作流 - 代码质量报告",
            "=" * 60,
            f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"检查文件数: {len(reports)}",
            "",
            "-" * 60,
            "总体评分",
            "-" * 60,
        ]
        
        # 计算平均分
        avg_format = sum(r.format_score for r in reports) / len(reports)
        avg_security = sum(r.security_score for r in reports) / len(reports)
        avg_quality = sum(r.quality_score for r in reports) / len(reports)
        avg_overall = sum(r.overall_score for r in reports) / len(reports)
        
        report_lines.extend([
            f"格式评分: {avg_format:.1%}",
            f"安全评分: {avg_security:.1%}",
            f"质量评分: {avg_quality:.1%}",
            f"总体评分: {avg_overall:.1%}",
            "",
        ])
        
        # 收集所有问题
        all_issues = []
        for report in reports:
            for issue in report.issues:
                all_issues.append({
                    **issue,
                    "file": report.file_path
                })
        
        if all_issues:
            report_lines.extend([
                "-" * 60,
                "发现的问题",
                "-" * 60,
            ])
            
            # 按严重程度排序
            severity_order = {"high": 0, "medium": 1, "warning": 2, "info": 3}
            all_issues.sort(key=lambda x: severity_order.get(x["severity"], 4))
            
            for i, issue in enumerate(all_issues, 1):
                report_lines.extend([
                    f"{i}. [{issue['severity'].upper()}] {issue['message']}",
                    f"   文件: {issue['file']}",
                    f"   详情: {issue['details']}",
                    "",
                ])
        
        # 收集所有建议
        all_suggestions = []
        for report in reports:
            all_suggestions.extend(report.suggestions)
        
        if all_suggestions:
            # 去重
            unique_suggestions = list(set(all_suggestions))
            report_lines.extend([
                "-" * 60,
                "改进建议",
                "-" * 60,
            ])
            
            for i, suggestion in enumerate(unique_suggestions, 1):
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
        print("使用方法: python code_quality_checker.py <文件路径或目录>")
        print("示例: python code_quality_checker.py src/")
        sys.exit(1)
    
    target = sys.argv[1]
    checker = CodeQualityChecker()
    reports = []
    
    if os.path.isfile(target):
        # 检查单个文件
        if target.endswith('.py'):
            report = checker.check_python_code(target)
            reports.append(report)
        elif target.endswith(('.js', '.ts', '.jsx', '.tsx')):
            report = checker.check_javascript_code(target)
            reports.append(report)
        else:
            print(f"不支持的文件类型: {target}")
            sys.exit(1)
    
    elif os.path.isdir(target):
        # 检查目录中的所有文件
        for root, dirs, files in os.walk(target):
            # 跳过隐藏目录和node_modules
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
            
            for file in files:
                file_path = os.path.join(root, file)
                
                if file.endswith('.py'):
                    report = checker.check_python_code(file_path)
                    reports.append(report)
                elif file.endswith(('.js', '.ts', '.jsx', '.tsx')):
                    report = checker.check_javascript_code(file_path)
                    reports.append(report)
    
    else:
        print(f"路径不存在: {target}")
        sys.exit(1)
    
    # 生成报告
    report = checker.generate_report(reports)
    print(report)
    
    # 保存报告到文件
    report_file = f"quality_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n报告已保存到: {report_file}")


if __name__ == "__main__":
    main()
