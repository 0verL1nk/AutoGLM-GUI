"""
Phone Agent - An AI-powered phone automation framework.

This package provides tools for automating Android and iOS phone interactions
using AI models for visual understanding and decision making.
"""

from phone_agent.agent import PhoneAgent

# from phone_agent.agent_ios import IOSPhoneAgent  # NOTE: kept for reference; not wired into AutoGLM_GUI.
__version__ = "0.1.0"
# TODO: iOS agent integration is not wired into AutoGLM_GUI yet.
__all__ = ["PhoneAgent"]
# __all__ = ["PhoneAgent", "IOSPhoneAgent"]  # NOTE: reference for legacy export list.
